from duck.duck import Duck
from flybehavior.fly_with_wings import FlyWithWings

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        
    def display(self):
        print("Display MallardDuck")