from abc import *

# Observer = Subscriber
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, value):
        pass