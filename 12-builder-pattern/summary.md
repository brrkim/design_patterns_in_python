# Builder

- when piecewise object construction is complicated, provide an API for doing it succinctly

## Motivation

- some objects are simple and can be created in a single initializer call
- sometimes other objects require a lot of ceremony to create (you have to build up the object in stages and it takes lots of time)
- having an object with 10 initializers would be solution but it is not productive
- instead, opt for piecewise construction
  - call different methods of a special component called a builder which actually allows you to do that
- builder provides an API for constructing an object step-by-step

## Summary
