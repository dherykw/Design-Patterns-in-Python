class Beverage:
    def get_description(self):
        raise NotImplementedError('you must implement this method')

    def get_cost(self):
        raise NotImplementedError('you must implement this method')

    def print(self):
        print("\nBeverage: {}. \nCost: {}".format(self.get_description(), self.get_cost()))


# This interface is only for doing the code more readable
class Condiment(Beverage):
    def get_cost(self):
        raise NotImplementedError('you must implement this method')

    def get_description(self):
        raise NotImplementedError('you must implement this method')


class Espresso(Beverage):
    def get_cost(self):
        return 0.90

    def get_description(self):
        return "Espresso"


class DarkRoast(Beverage):
    def get_cost(self):
        return 1.10

    def get_description(self):
        return "Dark Roast"


class Mocha(Condiment):
    def __init__(self, b: Beverage):
        self.beverage = b

    def get_cost(self):
        return .20 + self.beverage.get_cost()

    def get_description(self):
        return "{}, Mocha".format(self.beverage.get_description())


class Milk(Condiment):
    def __init__(self, b: Beverage):
        self.beverage = b

    def get_cost(self):
        return .10 + self.beverage.get_cost()

    def get_description(self):
        return "{}, Milk".format(self.beverage.get_description())


class Soy(Condiment):
    def __init__(self, b: Beverage):
        self.beverage = b

    def get_cost(self):
        return .15 + self.beverage.get_cost()

    def get_description(self):
        return "{}, Soy".format(self.beverage.get_description())


if __name__ == '__main__':
    beverage = Espresso()
    beverage = Mocha(beverage)
    beverage = Mocha(beverage)
    beverage.print()

    beverage = DarkRoast()
    beverage = Soy(beverage)
    beverage = Mocha(beverage)
    beverage.print()


