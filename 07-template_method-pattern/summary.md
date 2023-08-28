Template Method: A High-level blueprint for an algorithm to be completed by inheritators

Algorithms can be decomposed into common parts + specifics
Strategy pattern does this through (object) composition

- high-level algorithm expect strategies to conform to an interface
- concrete implementations implement the interface
  Template Method does this through inheritance
- define base class including abstract members
- inheritators override the abstract members
- tempalte method invoked to get work done

Template Method: Allow us to define the skeleton(바디가 비어있는 코드) of the algorithm,
with concrete implementations defined in subclasses.
