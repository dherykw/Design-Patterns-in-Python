class Strategy:
    def do_operation(self, a, b):
        raise NotImplementedError('you must implement this method')


class DoOperationAdd(Strategy):
    def do_operation(self, a, b):
        print("I am adding")
        return a + b


class DoOperationSubtract(Strategy):
    def do_operation(self, a, b):
        print("I am subtracting")
        return a - b


class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, a, b):
        return self.strategy.do_operation(a, b)

    def set_strategy(self, new_strategy):
        self.strategy = new_strategy


if __name__ == '__main__':
    context = Context(DoOperationAdd())
    print("The answer is: %s" % context.execute_strategy(5, 5))

    print("\n Changing the Strategy..")
    context.set_strategy(DoOperationSubtract())
    print("The answer of the new Strategy is: %s" % context.execute_strategy(5, 5))
