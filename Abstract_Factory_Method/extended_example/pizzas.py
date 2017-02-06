from .ingredients_factories import PizzaIngredientFactory


class PizzasTypes(enumerate):
    CHEESE = 1
    CLAM = 2


class Pizza:
    TYPE = PizzasTypes

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies = []
        self.pepperoni = None
        self.clam = None

    def prepare(self):
        raise NotImplementedError('You must implement this method')

    def bake(self):
        print("Bake for 25 minutes at 180ºC.")

    def cut(self):
        print("Cutting the pizza into diagonal slices.")

    def box(self):
        print("Place pizza in official PizzaStore Box.")


class CheesePizza(Pizza):
    def __init__(self, name, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.name = name
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing {}".format(self.name))
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, name, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.name = name
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing {}".format(self.name))
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clams()
