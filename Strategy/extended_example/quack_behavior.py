class QuackBehavior:
    def quack(self):
        raise NotImplementedError('you must implement this method')


class Quack(QuackBehavior):
    def quack(self):
        print("Hear my awesome quacking")


class Squeak(QuackBehavior):
    def quack(self):
        print("I squeak like a charm")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("I am mute dude!!, I can't")
