from simple_subject import SimpleSubject
from simple_observer import SimpleObserver

simple_subject = SimpleSubject()
simple_observer = SimpleObserver(simple_subject)
simple_subject.set_value(80)
