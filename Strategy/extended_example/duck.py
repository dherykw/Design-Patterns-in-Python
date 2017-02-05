from Strategy.extended_example.fly_behavior import FlyWithWings, FlyNoWay, FlyRockedPowered, FlyBehavior
from Strategy.extended_example.quack_behavior import Quack, Squeak, MuteQuack, QuackBehavior


class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    def display(self):
        raise NotImplementedError('you must implement this method')


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I am a great Mallard Duck")


class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("I am a Rubber Duck")


class MuteDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), MuteQuack())

    def display(self):
        print("I am a Mute Duck")


if __name__ == '__main__':
    mallard_duck = MallardDuck()
    rubber_duck = RubberDuck()
    mute_duck = MuteDuck()

    print(" ----------- Ducks Quacking -------------")
    mallard_duck.perform_quack()
    rubber_duck.perform_quack()
    mute_duck.perform_quack()

    print("\n ----------- Ducks Flying -------------")
    mallard_duck.perform_fly()
    rubber_duck.perform_fly()
    mute_duck.perform_fly()

    print("\n ----------- Giving Super Powers -------------")
    mute_duck.fly_behavior = FlyRockedPowered()
    mute_duck.perform_fly()
