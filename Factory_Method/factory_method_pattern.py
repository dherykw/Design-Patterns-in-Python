class Factory:
    def factory_method_create_product(self, type_):
        raise NotImplementedError('you must implement this method')

    def do_operation(self, type_):
        product = self.factory_method_create_product(type_)
        product.do_something()


class ConcreteFactory1(Factory):
    def factory_method_create_product(self, type_):
        if type_ is "Blue":
            return BlueProduct1()
        elif type_ is "Red":
            return RedProduct1()
        elif type_ is "Green":
            return GreenProduct1()


class ConcreteFactory2(Factory):
    def factory_method_create_product(self, type_):
        if type_ is "Blue":
            return BlueProduct2()
        elif type_ is "Red":
            return RedProduct2()
        elif type_ is "Green":
            return GreenProduct2()


class Product:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        print("I am {} and I am doing something".format(self.name))


class BlueProduct1(Product):
    def __init__(self):
        super().__init__("Blue Product 1")


class RedProduct1(Product):
    def __init__(self):
        super().__init__("Red Product 1")


class GreenProduct1(Product):
    def __init__(self):
        super().__init__("Green Product 1")


class BlueProduct2(Product):
    def __init__(self):
        super().__init__("Blue Product 2")


class RedProduct2(Product):
    def __init__(self):
        super().__init__("Red Product 2")


class GreenProduct2(Product):
    def __init__(self):
        super().__init__("Green Product 2")


if __name__ == "__main__":
    print("\n ----- Concrete Factory ----- \n")

    concrete_factory = ConcreteFactory1()
    concrete_factory.do_operation("Green")
    concrete_factory.do_operation("Blue")
    concrete_factory.do_operation("Red")

    print("\n ----- Other Factory ----- \n")

    other_factory = ConcreteFactory2()
    other_factory.do_operation("Green")
    other_factory.do_operation("Blue")
    other_factory.do_operation("Red")
