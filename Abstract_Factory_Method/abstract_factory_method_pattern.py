class AbstractFactory:
    def CreateProductA(self):
        raise NotImplementedError('You must implement this method')

    def CreateProductB(self):
        raise NotImplementedError('You mut implement this method')


class ConcreteFactory1(AbstractFactory):
    def CreateProductA(self):
        pass

    def CreateProductB(self):
        pass


class ConcreteFactory2(AbstractFactory):
    def CreateProductA(self):
        pass

    def CreateProductB(self):
        pass


class AbstractProductA:
    pass


class ProductA1(AbstractProductA):
    def __init__(self):
        print("Product A1")


class ProductA2(AbstractProductA):
    def __init__(self):
        print("Product A2")


class AbstractProductB:
    pass


class ProductB1(AbstractProductB):
    def __init__(self):
        print("Product B1")


class ProductB2(AbstractProductB):
    def __init__(self):
        print("Product B2")


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
