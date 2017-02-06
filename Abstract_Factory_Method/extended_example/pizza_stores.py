from Abstract_Factory_Method.extended_example.pizzas import Pizza, CheesePizza, ClamPizza
from Abstract_Factory_Method.extended_example.ingredients_factories import NYPizzaIngredientsFactory, \
    ChicagoPizzaIngredientsFactory


class PizzaStore:
    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def create_pizza(self, type_):
        raise NotImplementedError('you must implement this method')


class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, type_):
        if type_ == Pizza.TYPE.CHEESE:
            return CheesePizza("New York Style Cheese Pizza", NYPizzaIngredientsFactory())
        elif type_ == Pizza.TYPE.CLAM:
            return ClamPizza("New York Style Calm Pizza", NYPizzaIngredientsFactory())


class ChicagoYorkPizzaStore(PizzaStore):
    def create_pizza(self, type_):
        if type_ == Pizza.TYPE.CHEESE:
            return CheesePizza("Chicago Style Cheese Pizza", ChicagoPizzaIngredientsFactory())
        elif type_ == Pizza.TYPE.CLAM:
            return ClamPizza("Chicago Style Calm Pizza", ChicagoPizzaIngredientsFactory())


if __name__ == "__main__":
    print("\n ---- NY Store Pizza ---- ")
    NYStore = NewYorkPizzaStore()
    pizza = NYStore.order_pizza(Pizza.TYPE.CHEESE)

    print("\n ---- Chicago Store Pizza ---- ")
    ChicagoStore = ChicagoYorkPizzaStore()
    pizza = ChicagoStore.order_pizza(Pizza.TYPE.CHEESE)
