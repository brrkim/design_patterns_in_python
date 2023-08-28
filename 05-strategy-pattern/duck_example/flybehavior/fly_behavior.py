from abc import *

class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): pass