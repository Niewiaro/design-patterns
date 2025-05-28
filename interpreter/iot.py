from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums, ParseException


class Boiler:
    def __init__(self):
        self.temperature = 83  # in celsius

    def __str__(self):
        return f'boiler temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the boiler's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the boiler's temperature by {amount} degrees")
        self.temperature -= amount


class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the air condition')
        self.is_on = True

    def turn_off(self):
        print('turning off the air condition')
        self.is_on = False


class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heating')
        self.is_on = False


class Fridge:
    def __init__(self):
        self.temperature = 2  # in celsius

    def __str__(self):
        return f'fridge temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the fridge's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the fridge's temperature by {amount} degrees")
        self.temperature -= amount


def main():
    # Parser configuration
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    # Initialize devices
    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    # Define available actions
    open_actions = {
        'gate': gate.open,
        'garage': garage.open,
        'air condition': airco.turn_on,
        'heating': heating.turn_on,
        'boiler temperature': boiler.increase_temperature,
        'fridge temperature': fridge.increase_temperature
    }
    
    close_actions = {
        'gate': gate.close,
        'garage': garage.close,
        'air condition': airco.turn_off,
        'heating': heating.turn_off,
        'boiler temperature': boiler.decrease_temperature,
        'fridge temperature': fridge.decrease_temperature
    }

    print("Smart Home Control System")
    print("Available commands examples:")
    print("- open -> gate")
    print("- close -> garage") 
    print("- turn on -> air condition")
    print("- turn off -> heating")
    print("- increase -> boiler temperature -> 5 degrees")
    print("- decrease -> fridge temperature -> 2 degrees")
    print("Type 'exit' to quit")
    print("Type 'status' to see devices state")

    while True:
        try:
            command = input("\nEnter command: ").strip()
            
            if command.lower() == 'exit':
                break
                
            if command.lower() == 'status':
                print("\nCurrent devices state:")
                print(f"Gate: {gate}")
                print(f"Garage: {garage}")
                print(f"Air condition: {airco}")
                print(f"Heating: {heating}")
                print(f"Boiler: {boiler}")
                print(f"Fridge: {fridge}")
                continue

            # Parse and execute command
            try:
                parsed = event.parseString(command)
                
                if len(parsed) == 2:  # No argument
                    cmd, dev = parsed
                    cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
                    
                    if 'open' in cmd_str or 'turn on' in cmd_str:
                        open_actions[dev_str]()
                    elif 'close' in cmd_str or 'turn off' in cmd_str:
                        close_actions[dev_str]()
                        
                elif len(parsed) == 3:  # With argument
                    cmd, dev, arg = parsed
                    cmd_str = ' '.join(cmd)
                    dev_str = ' '.join(dev)
                    arg_str = ' '.join(arg)
                    
                    try:
                        num_arg = int(arg_str.split()[0])
                        if num_arg <= 0:
                            print("Error: Temperature change must be positive")
                            continue
                            
                        if 'increase' in cmd_str:
                            open_actions[dev_str](num_arg)
                        elif 'decrease' in cmd_str:
                            close_actions[dev_str](num_arg)
                            
                    except ValueError:
                        print(f"Error: Invalid number format in '{arg_str}'")
                        
            except ParseException:
                print("Error: Invalid command format")
            except KeyError:
                print("Error: Unknown device or command")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()