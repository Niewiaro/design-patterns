quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...',
    'Facts are stubborn things.',
    'Why do programmers prefer dark mode? Because light attracts bugs.',
    'There are 10 types of people in the world: those who understand binary and those who don\'t.',
    'Don\'t worry if plan A fails, there are 25 more letters in the alphabet.',
    'My bed is a magical place where I suddenly remember everything I had to do.',
)


class QuoteModel:
    def get_quote(self, n):
        try:
            return quotes[n]
        except IndexError:
            return 'Not found!'


class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input("Enter quote number (or 'q' to quit): ")


class FancyQuoteView:
    def show(self, quote):
        length = len(quote)
        amount = 50 if length < 50 else length + 20
        print("=" * amount)
        print(f'"{quote}"'.center(amount))
        print("=" * amount)

    def error(self, msg):
        print("!" * 50)
        print(f'ERROR: {msg}'.center(50))
        print("!" * 50)

    def select_quote(self):
        return input("Enter quote number (or 'q' to quit): ")

class CrazyTerminalView:
    def show(self, quote):
        result = quote.replace(' ', '*')
        result = result[::-1]
        result = result.swapcase()
        print(f'And the quote is: "{result}"')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input("Enter quote number (or 'q' to quit): ")


class QuoteTerminalController:
    def __init__(self, view):
        self.model = QuoteModel()
        self.view = view

    def run(self):
        user_input = self.view.select_quote()

        if user_input.lower() == 'q':
            return False

        try:
            n = int(user_input)
        except ValueError:
            self.view.error(f"Incorrect input '{user_input}'")
            return True

        quote = self.model.get_quote(n)
        self.view.show(quote)
        return True


def choose_view():
    print("Choose a view:")
    print("1 - Standard view")
    print("2 - Fancy view")
    print("3 - Crazy view")

    valid_input = False
    choice = None

    while not valid_input:
        choice = input("Enter your choice: ")
        if choice in ('1', '2', '3'):
            valid_input = True
        else:
            print("Incorrect input. Please try again.")
    if choice == '1':
        return QuoteTerminalView()
    elif choice == '2':
        return FancyQuoteView()
    else:
        return CrazyTerminalView()


def main():
    view = choose_view()
    controller = QuoteTerminalController(view)

    while controller.run():
        pass

    print("Goodbye!")


if __name__ == "__main__":
    main()
