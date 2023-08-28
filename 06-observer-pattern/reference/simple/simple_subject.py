from subject import Subject
from observer import Observer

class SimpleSubject(Subject):
    _observers: list
    _value: int = 0
    
    def __init__(self):
        self._observers = []
    
    def register_observer(self, o: Observer):
        self._observers.append(o)
    
    def remove_observer(self, o: Observer):
        idx = self._observers.index(o)
        if idx: 
            self._observers.pop(idx)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._value)
    
    def set_value(self, value):
        self._value = value
        self.notify_observers()