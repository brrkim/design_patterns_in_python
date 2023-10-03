# Singleton

- A component which is instantiated only once
  - and then everybody who tries to access this object basically gets to work with that one instance
- A design pattern everyone loves to hate but is it really that bad?

## Motivation

- for some components it only makes sense to have one in the system
  - database repository
  - object factory (stateless, no attributes worth assigning, simply use static methods)
- initializer call is expensive
  - we only do it once
  - we provide everyone with the same instance
- want to prevent anyone creating additional copies
- need to take care of lazy instantiation
  - initialize it only when somebody actually asked for it

## Summary

- Different realizations of singleton: custom allocator, decorator, metaclass
- Laziness is easy, just init on first request
- Monostate Variation
  - bazaar variation on singleton, where objects appear as normal object but they all map to a single dictionary.
- Testability issues
  - problem
    - Real DB에서 live data에서 업데이트될 때 테스트케이스가 깨지는 상황이 생길 수 있음
  - solving
    - live data를 사용하지 말고, Mocking DB의 dummy data를 사용하자
