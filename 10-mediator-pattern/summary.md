# Mediator (중간자)

- A component that **facilitates communication between different components** without them necessarily being aware of each other or having direct (reference) access to each other

## Motivation

- in system with many components, you know the components can go in and out of the system at any time
  - chat room participants
    - they all kinds of join the room, leave the room, ...
  - MMORPG players
- direct references to one another --> make no sense
  - references may go dead
- solution: participants refer to some central component that facilitates communication

## Summary

1. create the mediator and have each object in the system refer to it (typically it's in a property and stick mediator inside initializer)
2. Mediator engages in bidirectional communication with it's connected components
3. mediator has functions the components can call
4. components have functions the mediator can call
5. Event processing libs make communication easier
