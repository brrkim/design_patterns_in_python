State: Fun with Finite State Machines.

- Motivation

  - Changes in state can be explicit or in response to event (Observer pattern)

- State

  - A pattern in which the object's behavior is determined by its state.
  - An object transitions from one state to another
  - A formalized construct which manages state and transitions is called a state machine.

- Summary
  - given sufficient complexitym it pays to formally define possible states and events/triggers
    - useful to define formally define states as well as possible transition from one state to another.
  - can define
    - behavior of a state entry and exit
    - actions when a particular event causes a transition.
    - guard condition enabling/disabling a transition
    - default action when no transitions are found for an event
