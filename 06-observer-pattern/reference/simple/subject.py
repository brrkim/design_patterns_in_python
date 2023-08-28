from abc import *
from observer import Observer

# Subject = Publisher = Observable
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, o:Observer):
        pass
    
    @abstractmethod
    def remove_observer(self, o:Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass