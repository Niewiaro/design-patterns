import pickle


class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def save_state(self):
        current_state = pickle.dumps(self.__dict__)
        return current_state

    def restore_state(self, memento):
        previous_state = pickle.loads(memento)
        self.__dict__.clear()
        self.__dict__.update(previous_state)

    def __str__(self):
        return f'{self.text} - By {self.author}.'


def main():
    quotes = []
    states = []

    # Demo Quote 1
    q1 = Quote("A room without books is like a body without a soul.", 'Unknown author')
    quotes.append(q1)
    states.append([])
    print('Quote 1')
    print(f'\nOriginal version:\n{q1}')
    q1_mem = q1.save_state()
    states[0].append(q1_mem)
    q1.author = 'Marcus Tullius Cicero'
    print(f'\nWe found the author, and did an updated:\n{q1}')
    q1.restore_state(q1_mem)
    print(f'\nWe had to restore the previous version:\n{q1}\n')

    # Demo Quote 2
    q2 = Quote(
        "To be you in a world that is constantly trying to make you be something else is the greatest accomplishment.",
        'Ralph Waldo Emerson')
    quotes.append(q2)
    states.append([])
    print('Quote 2')
    print(f'\nOriginal version:\n{q2}')
    q2_mem1 = q2.save_state()
    states[1].append(q2_mem1)
    q2.text = "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment."
    print(f'\nWe fixed the text:\n{q2}')
    q2_mem2 = q2.save_state()
    states[1].append(q2_mem2)
    q2.text = "To be yourself when the world is constantly trying to make you something else is the greatest accomplishment."
    print(f'\nWe fixed the text again:\n{q2}')
    q2.restore_state(q2_mem2)
    print(f'\nWe had to restore the 2nd version, the correct one:\n{q2}\n')

    while True:
        print("\nMenu:")
        print("1. Add quote")
        print("2. List quotes")
        print("3. Edit quote")
        print("4. Save quote state")
        print("5. Restore quote state")
        print("6. Restore quote state with content")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            text = input("Enter quote text: ")
            author = input("Enter author: ")
            quotes.append(Quote(text, author))
            states.append([])
            print("Quote added.")
        elif choice == '2':
            for idx, q in enumerate(quotes):
                print(f"{idx}: {q}")
        elif choice == '3':
            idx = int(input("Quote index to edit: "))
            if 0 <= idx < len(quotes):
                quotes[idx].text = input("New text: ")
                quotes[idx].author = input("New author: ")
                print("Quote updated.")
            else:
                print("Invalid index.")
        elif choice == '4':
            idx = int(input("Quote index to save state: "))
            if 0 <= idx < len(quotes):
                memento = quotes[idx].save_state()
                states[idx].append(memento)
                print("State saved.")
            else:
                print("Invalid index.")
        elif choice == '5' or choice == '6':
            idx = int(input("Quote index to restore: "))
            if 0 <= idx < len(quotes):
                if not states[idx]:
                    print("No saved states.")
                    continue
                for s_idx in range(len(states[idx])):
                    if choice == '5':
                        print(f"{s_idx}: State {s_idx}")
                    else:
                        print(f"{s_idx}: State {s_idx}: {pickle.loads(states[idx][s_idx])}")
                s_choice = int(input("Choose state index to restore: "))
                if 0 <= s_choice < len(states[idx]):
                    quotes[idx].restore_state(states[idx][s_choice])
                    print("State restored.")
                else:
                    print("Invalid state index.")
            else:
                print("Invalid quote index.")
        elif choice == '7':
            break
        else:
            print("Invalid option.")


if __name__ == '__main__':
    main()
