class FlyBehavior:
    def fly(self):
        raise NotImplementedError('you must implement this method')


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I am trying!! but I cant 8_( ")


class FlyRockedPowered(FlyBehavior):
    def fly(self):
        print("I have rocket super powers")
