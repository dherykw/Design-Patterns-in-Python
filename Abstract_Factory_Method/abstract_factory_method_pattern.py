class AbstractFactory:
    def create_product_A(self):
        raise NotImplementedError('You must implement this method')

    def create_product_B(self):
        raise NotImplementedError('You mut implement this method')


class ConcreteFactory1(AbstractFactory):
    def create_product_A(self):
        return ProductA1()

    def create_product_B(self):
        return ProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_A(self):
        return ProductA2()

    def create_product_B(self):
        return ProductB2()


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


class Client:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def create_products(self):
        self.factory.create_product_A()
        self.factory.create_product_B()


if __name__ == "__main__":
    print("\n ----- Concrete Factory ----- \n")

    client = Client(ConcreteFactory1())
    client.create_products()

    print("\n ----- Other Factory ----- \n")

    client = Client(ConcreteFactory2())
    client.create_products()
