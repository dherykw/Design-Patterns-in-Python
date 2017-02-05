class PizzasTypes(enumerate):
    CHEESE = 1


class Pizza:

    TYPE = PizzasTypes

    def __init__(self, name, dough, sauce):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough... ")
        print("Adding sauce... ")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(" {}".format(topping))

    def bake(self):
        print("Bake for 25 minutes at 180ºC.")

    def cut(self):
        print("Cutting the pizza into diagonal slices.")

    def box(self):
        print("Place pizza in official PizzaStore Box.")


class NewYorkStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name="NY Style Sauce and Cheese Pizza",
            dough="Thin Crust Dough",
            sauce="Marinara Sauce"
        )
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name="Chicago Style Deep Dish Cheese Pizza",
            dough="Extra Thick Crust Dough",
            sauce="Plum Tomato Sauce"
        )
        self.toppings.append("Grated Reggiano Cheese")
