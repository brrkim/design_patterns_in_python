Well, the motivation for using the Observer is that sometimes in our system we need to be informed
when a certain thing happened and that can be virtually anything.

Another thing we might want to watch for is whenever an object does something, so whenever you have
a class which does a particular thing, you might want to get a notification on it, maybe like a real
human notification so somebody can take a look at this operation and determine whether it was invalid or not.


So the observer design pattern actually involves two concepts.
1) you have the observer, and the observer is the object that wishes to be informed
about something else happening in the system 
2) and the entity which actually generates those events, which we want to observe is typically called an observable.

So the observable is the generator of the events, and the observer is the consumer of the events that
get the notifications and can decide on what to do with them.


In Python,
Event + Property = Property Observers
Property Observer tells you whenever a property is actually changed.


Property observers seemed like a really nice thing to have a really nice implementation that we'll tell
you whenever a property changes.
Unfortunately, there are problems with them.
And one problem is what happens when you have a property that's dependent on another property.


So this probably has a GETER.
It obviously has no center since this is a computer property.
But now we have a problem.
How do we send notifications on changes to the voting ability of a person?



1) So we saw that observer is generally an intrusive approach.
You basically have to jump into the class and perform modifications so as to expose some sort of event
that people can subscribe to.
2) Now subscription and unsubscription is fairly easy, at least it is in the implementation that I have
shown in the sense that an event is quite simply a list of a function references, and then what you
do to subscribe and unsubscribe is you add to that list and you remove from that list that allows easy
subscription and unsubscription.
3) And finally, we looked at property observers and we saw that in the general case where you have just
individual independent properties, then property notifications are really easy.
However, if you have properties depending on other properties, then those notifications get significantly more difficult.
