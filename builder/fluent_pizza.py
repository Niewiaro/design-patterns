import time
from enum import Enum

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano pineapple')

STEP_DELAY = 1


class Pizza:
    def __init__(self, builder):
        self.name = builder.name
        self.dough = builder.dough
        self.sauce = builder.sauce
        self.topping = builder.topping
        self.baking_time = builder.baking_time
        self.progress = builder.progress

    def __str__(self):
        return (f'Pizza "{self.name}" with {self.dough.name} dough, '
                f'{self.sauce.name if self.sauce else "no"} sauce, '
                f'toppings: {', '.join([t.name for t in self.topping])} '
                f'is {self.progress.name}')

    class PizzaBuilder:
        def __init__(self, name: str, baking_time: int = 5):
            self.name = name
            self.progress = PizzaProgress.queued
            self.baking_time = baking_time
            self.dough = None
            self.sauce = None
            self.topping = []

        def prepare_dough(self, dough: str):
            self.progress = PizzaProgress.preparation
            self.dough = PizzaDough[dough]
            print(f'Preparing the {self.dough.name} dough for your {self.name}...')
            time.sleep(STEP_DELAY)
            print(f'Done with the {self.dough.name} dough.')
            return self

        def add_sauce(self, sauce: str):
            self.sauce = PizzaSauce[sauce]
            print(f'Adding the {self.sauce.name} sauce to your {self.name}...')
            time.sleep(STEP_DELAY)
            print(f'Done with the {self.sauce.name} sauce.')
            return self

        def add_topping(self, toppings: list[str]):
            print(f'Adding toppings to your {self.name}: {", ".join(toppings)}')
            for t in toppings:
                self.topping.append(PizzaTopping[t])
            time.sleep(STEP_DELAY)
            print('Done with the toppings.')
            return self

        def bake(self):
            self.progress = PizzaProgress.baking
            print(f'Baking your {self.name} for {self.baking_time} seconds...')
            time.sleep(self.baking_time)
            self.progress = PizzaProgress.ready
            print(f'Your {self.name} is ready!')
            return Pizza(self)


def main() -> None:
    pizza = (Pizza.PizzaBuilder('fluent').prepare_dough('thin').add_sauce('tomato').add_topping(
        ['mozzarella', 'ham', 'pineapple']).bake())
    print(pizza)


if __name__ == '__main__':
    main()

# Klasyczny builder zapewnia większą kontrolę i lepszą czytelność przy złożonej logice budowy obiektu.
# Fluent builder oferuje bardziej zwięzłą i czytelną składnię, lepszą do prostych i liniowych konstrukcji.
# Fluent builder może być trudniejszy do debugowania i wymaga konsekwentnego zwracania self.
# W przypadku prostych obiektów (np. pizza) fluent builder jest bardziej czytelny i preferowany.
