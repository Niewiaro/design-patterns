class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' " \
               f"has data = {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify()


class HexFormatterObs:
    def notify(self, publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex "
              f"data = {value}")


class BinaryFormatterObs:
    def notify(self, publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin "
              f"data = {value}")


class OctalFormatterObs:
    def notify(self, publisher):
        value = oct(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now oct "
              f"data = {value}")


class RomanFormatterObs:
    def notify(self, publisher):
        def to_roman(num):
            val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
            roman_num = ''
            i = 0
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num

        value = to_roman(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now roman "
              f"data = {value}")


class ScientificFormatterObs:
    def notify(self, publisher):
        value = f"{publisher.data:e}"
        print(f"{type(self).__name__}: '{publisher.name}' has now scientific "
              f"data = {value}")


def main():
    df = DefaultFormatter('test1')
    hf = HexFormatterObs()
    bf = BinaryFormatterObs()
    of = OctalFormatterObs()
    rf = RomanFormatterObs()
    sf = ScientificFormatterObs()

    while True:
        print("\nMenu:")
        print("1. Show current state")
        print("2. Add hex observer")
        print("3. Add binary observer")
        print("4. Add octal observer")
        print("5. Add roman observer")
        print("6. Add scientific observer")
        print("7. Remove hex observer")
        print("8. Remove binary observer")
        print("9. Remove octal observer")
        print("10. Remove roman observer")
        print("11. Remove scientific observer")
        print("12. Set new value")
        print("13. Exit")

        choice = input("\nEnter your choice (1-13): ")

        if choice == '1':
            print(df)
        elif choice == '2':
            df.add(hf)
            print("Hex observer added")
        elif choice == '3':
            df.add(bf)
            print("Binary observer added")
        elif choice == '4':
            df.add(of)
            print("Octal observer added")
        elif choice == '5':
            df.add(rf)
            print("Roman observer added")
        elif choice == '6':
            df.add(sf)
            print("Scientific observer added")
        elif choice == '7':
            df.remove(hf)
            print("Hex observer removed")
        elif choice == '8':
            df.remove(bf)
            print("Binary observer removed")
        elif choice == '9':
            df.remove(of)
            print("Octal observer removed")
        elif choice == '10':
            df.remove(rf)
            print("Roman observer removed")
        elif choice == '11':
            df.remove(sf)
            print("Scientific observer removed")
        elif choice == '12':
            new_value = input("Enter new value: ")
            df.data = new_value
        elif choice == '13':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
