from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)


@acts_as_state_machine
class TicketReservation:
    """
    A state machine implementation for a ticket reservation system.
    
    States:
    - available: Initial state, ticket is available for reservation
    - selected: A user has selected ticket
    - reserved: Ticket has been temporarily reserved
    - paid: Ticket has been paid for and confirmed
    - cancelled: Reservation has been canceled
    
    Events:
    - select_seat: Move from available to selected
    - make_reservation: Move from selected to reserved
    - make_payment: Move from reserved to paid
    - cancel: Move to cancel from selected or reserved
    - release: Return ticket to available state from selected or reserved
    """
    
    # States definition
    available = State(initial=True)
    selected = State()
    reserved = State()
    paid = State()
    cancelled = State()
    
    # Events definition
    select_seat = Event(from_states=available,
                       to_state=selected)
    
    make_reservation = Event(from_states=selected,
                           to_state=reserved)
    
    make_payment = Event(from_states=reserved,
                        to_state=paid)
    
    cancel = Event(from_states=(selected, reserved),
                  to_state=cancelled)
    
    release = Event(from_states=(selected, reserved, cancelled),
                   to_state=available)

    def __init__(self, ticket_id, seat_number):
        """
        Initialize a new ticket reservation.
        
        Args:
            ticket_id (str): Unique identifier for the ticket
            seat_number (str): Seat number associated with the ticket
        """
        self.ticket_id = ticket_id
        self.seat_number = seat_number
        self.customer_name = None
        self.reservation_time = None
        
    # State transition callbacks
    @after('select_seat')
    def on_select(self):
        print(f'Seat {self.seat_number} has been selected')

    @after('make_reservation')
    def on_reserve(self):
        print(f'Seat {self.seat_number} has been reserved')

    @before('make_payment')
    def on_payment(self):
        print(f'Processing payment for seat {self.seat_number}')

    @after('make_payment')
    def after_payment(self):
        print(f'Payment confirmed for seat {self.seat_number}')

    @after('cancel')
    def on_cancel(self):
        print(f'Reservation for seat {self.seat_number} has been cancelled')

    @after('release')
    def on_release(self):
        print(f'Seat {self.seat_number} has been released back to available pool')
        self.customer_name = None
        self.reservation_time = None


def transition(ticket, event, event_name):
    """
    Safely attempt a state transition.
    
    Args:
        ticket (TicketReservation): The ticket to transition
        event (Event): The event to trigger
        event_name (str): Name of the event for error reporting
    """
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: Cannot {event_name} ticket (ID: {ticket.ticket_id}) - invalid transition from {ticket.current_state}')


def get_ticket_status(ticket):
    """
    Print the current status of a ticket.
    
    Args:
        ticket (TicketReservation): The ticket to check
    """
    print(f'Ticket ID: {ticket.ticket_id}, Seat: {ticket.seat_number}, Status: {ticket.current_state}')


def main():
    # Create some test tickets
    ticket1 = TicketReservation("T001", "A1")
    ticket2 = TicketReservation("T002", "B2")
    
    # Display initial status
    print("Initial status:")
    get_ticket_status(ticket1)
    get_ticket_status(ticket2)
    print()
    
    # Test a normal booking flow
    print("Normal booking flow for Ticket 1:")
    transition(ticket1, ticket1.select_seat, "select")
    transition(ticket1, ticket1.make_reservation, "reserve")
    transition(ticket1, ticket1.make_payment, "pay")
    get_ticket_status(ticket1)
    print()
    
    # Test cancellation flow
    print("Cancellation flow for Ticket 2:")
    transition(ticket2, ticket2.select_seat, "select")
    transition(ticket2, ticket2.make_reservation, "reserve")
    transition(ticket2, ticket2.cancel, "cancel")
    transition(ticket2, ticket2.release, "release")
    get_ticket_status(ticket2)
    print()
    
    # Test invalid transition
    print("Testing invalid transition:")
    transition(ticket2, ticket2.make_payment, "pay")  # Should fail as ticket is available


if __name__ == '__main__':
    main()