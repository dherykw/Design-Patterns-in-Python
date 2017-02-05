class Creator:
    def factory_method_create_product(self, type_):
        raise NotImplementedError('you must implement this method')

    def do_operation(self, type_):
        product = self.factory_method_create_product(type_)
        product.do_something()


class ConcreteCreator(Creator):
    def factory_method_create_product(self, type_):
        if type_ is "Blue":
            return ConcreteBlueProduct()
        elif type_ is "Red":
            return ConcreteRedProduct()
        elif type_ is "Green":
            return ConcreteGreenProduct()


class OtherCreator(Creator):
    def factory_method_create_product(self, type_):
        if type_ is "Blue":
            return OtherBlueProduct()
        elif type_ is "Red":
            return OtherRedProduct()
        elif type_ is "Green":
            return OtherGreenProduct()


class Product:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        print("I am {} and I am doing something".format(self.name))


class ConcreteBlueProduct(Product):
    def __init__(self):
        super().__init__("Concrete Blue Product")


class ConcreteRedProduct(Product):
    def __init__(self):
        super().__init__("Concrete Red Product")


class ConcreteGreenProduct(Product):
    def __init__(self):
        super().__init__("Concrete Green Product")


class OtherBlueProduct(Product):
    def __init__(self):
        super().__init__("Other Blue Product")


class OtherRedProduct(Product):
    def __init__(self):
        super().__init__("Other Red Product")


class OtherGreenProduct(Product):
    def __init__(self):
        super().__init__("Other Green Product")


if __name__ == "__main__":
    print("\n ----- Concrete Factory ----- \n")

    concrete_factory = ConcreteCreator()
    concrete_factory.do_operation("Green")
    concrete_factory.do_operation("Blue")
    concrete_factory.do_operation("Red")

    print("\n ----- Other Factory ----- \n")

    other_factory = OtherCreator()
    other_factory.do_operation("Green")
    other_factory.do_operation("Blue")
    other_factory.do_operation("Red")
