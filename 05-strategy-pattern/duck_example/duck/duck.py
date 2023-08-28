from abc import *
from flybehavior.fly_behavior import FlyBehavior

class Duck(metaclass=ABCMeta):
    fly_behavior:FlyBehavior
    
    def set_fly_behavior(self,fb:FlyBehavior):
        self.fly_behavior = fb
        
    def perform_fly(self):
        self.fly_behavior.fly()
        
    # Duck native attr
    def swim(self):
        print("swin")
    
    @abstractmethod
    def display(self):
        pass