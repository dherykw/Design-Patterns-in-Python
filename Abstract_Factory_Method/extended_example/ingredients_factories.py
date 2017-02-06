from .ingredients import *


class PizzaIngredientFactory:
    def create_dough(self):
        raise NotImplementedError('you must implement this method')

    def create_sauce(self):
        raise NotImplementedError('you must implement this method')

    def create_cheese(self):
        raise NotImplementedError('you must implement this method')

    def create_veggies(self):
        raise NotImplementedError('you must implement this method')

    def create_peperoni(self):
        raise NotImplementedError('you must implement this method')

    def create_clams(self):
        raise NotImplementedError('you must implement this method')


class NYPizzaIngredientsFactory(PizzaIngredientFactory):
    def create_clams(self):
        return FreshClams()

    def create_cheese(self):
        return ReggianoCheese()

    def create_peperoni(self):
        return SlicedPeperoni()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()


class ChicagoPizzaIngredientsFactory(PizzaIngredientFactory):
    def create_clams(self):
        return FrozenClams()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_peperoni(self):
        return SlicedPeperoni()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()
