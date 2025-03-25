class Frog:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle) -> None:
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    def __str__(self) -> str:
        return 'a bug'

    def action(self) -> str:
        return 'eats it'


class FrogWorld:
    def __init__(self, name: str) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle) -> None:
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)


class Ork:
    def __str__(self) -> str:
        return 'an evil ork'

    def action(self) -> str:
        return 'kills it'


class WizardWorld:
    def __init__(self, name: str) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory) -> None:
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self) -> None:
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)


def main() -> None:
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == "__main__":
    main()
