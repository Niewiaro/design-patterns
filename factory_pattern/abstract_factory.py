import random


class Frog:
    def __init__(self, name: str) -> None:
        self.name = name
        self.energy = 10

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle) -> str | None:
        act = obstacle.action
        self.energy -= obstacle.health
        if self.energy <= 0:
            return None
        if obstacle.health == 1:
            msg = f'{self} the Frog encounters a {obstacle} and {act}!'
        else:
            msg = f'{self} the Frog encounters the {obstacle.health} {obstacle}s and {act}!'
        return msg


class Bug:
    def __str__(self) -> str:
        return 'bug'

    @property
    def action(self) -> str:
        return 'eats it'

    @property
    def health(self) -> int:
        return random.randint(1, 3)


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
        self.energy = 10000

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle) -> str | None:
        act = obstacle.action
        self.energy -= obstacle.health
        if self.energy <= 0:
            return None
        return f'{self} the Wizard battles against {obstacle} with {obstacle.health} health and {act}!'


class Ork:
    def __str__(self) -> str:
        return 'an evil ork'

    @property
    def action(self) -> str:
        return 'kills it'

    @property
    def health(self) -> int:
        return random.randint(100, 350)


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

    def play(self) -> str | None:
        return self.hero.interact_with(self.obstacle)


def validate_age(name: str, /, *, min_age: int = 1, max_age: int = 120, acceptable_age: int = 18,
                 max_attempts: int = 3) -> tuple[bool, int] | None:
    """
    Prompts the user for their age, validates that it's an integer, and checks if it falls within the given age range.

    Args:
        name (str): User's name, used in the prompt.
        min_age (int, optional): Minimum acceptable age (inclusive). Defaults to 1.
        max_age (int, optional): Maximum acceptable age (inclusive). Defaults to 120.
        acceptable_age (int, optional): The age considered acceptable for a certain action. Defaults to 18.
        max_attempts (int, optional): Maximum number of input attempts. Defaults to 3.

    Returns:
        Tuple[bool, int] | None: A tuple where the first element indicates success,
                                 and the second is the validated age. None on failure.
    """
    for attempt in range(max_attempts):
        try:
            age = int(input(f"Welcome {name}. How old are you?\n\tI am: "))
        except ValueError:
            print("Invalid input. Please enter a numeric age.")
            continue

        if not (min_age <= age <= max_age):
            print(f"Age must be between {min_age} and {max_age}. You entered: {age}")
            continue

        if age < acceptable_age:
            return False, age

        return True, age

    print("Too many invalid attempts.")
    return None


def main() -> None:
    name = input("Hello. What's your name?\n\tMy name is: ")

    result = validate_age(name)
    if result is None:
        return

    is_valid, _ = result
    game = WizardWorld if is_valid else FrogWorld
    environment = GameEnvironment(game(name))

    x = 0
    while True:
        result = environment.play()
        if result is None:
            break
        print(f"{x + 1}. {result}")
        x += 1

    print(f"END GAME\nSCORE: {x}!")


if __name__ == "__main__":
    main()
