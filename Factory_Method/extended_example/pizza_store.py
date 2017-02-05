from Factory_Method.extended_example.pizza import Pizza, NewYorkStyleCheesePizza, ChicagoStyleCheesePizza


class PizzaStore:
    def order_pizza(self, type_):
        pizza = self._create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def _create_pizza(self, type_):
        raise NotImplementedError('you must implement this method')


class NewYorkPizzaStore(PizzaStore):
    def _create_pizza(self, type_):
        if type_ == Pizza.TYPE.CHEESE:
            return NewYorkStyleCheesePizza()


class ChicagoYorkPizzaStore(PizzaStore):
    def _create_pizza(self, type_):
        if type_ == Pizza.TYPE.CHEESE:
            return ChicagoStyleCheesePizza()


if __name__ == "__main__":
    print("\n ---- NY Store Pizza ---- ")
    NYStore = NewYorkPizzaStore()
    pizza = NYStore.order_pizza(Pizza.TYPE.CHEESE)

    print("\n ---- Chicago Store Pizza ---- ")
    ChicagoStore = ChicagoYorkPizzaStore()
    pizza = ChicagoStore.order_pizza(Pizza.TYPE.CHEESE)
