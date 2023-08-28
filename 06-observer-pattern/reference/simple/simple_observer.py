from observer import Observer
from subject import Subject

class SimpleObserver(Observer):
    _value: int
    _simple_subject: Subject
    
    def __init__(self, simple_subject: Subject):
        self._simple_subject = simple_subject
        simple_subject.register_observer(self) # Subscribe
    
    def update(self, value):
        self._value = value
        self.display()
    
    def display(self):
        print(f"Value: {self._value}")