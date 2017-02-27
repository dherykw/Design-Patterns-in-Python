class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def get_instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Foo:
    def __init__(self):
        print('Foo created')
        self.x = 0

    def add(self):
        self.x += 1
        print('Foo added 1 = %s' % self.x)


if __name__ == '__main__':
    try:
        f = Foo()  # Error, this isn't how you get the instance of a singleton
    except TypeError:
        print("It is a singletone dude!!")

    f = Foo.get_instance()  # Good. Being explicit is in line with the Python Zen
    f.add()
    g = Foo.get_instance()  # Returns already created instance
    g.add()

    print('Are they the same instances? %s' % (f is g))
