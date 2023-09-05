# Factory Method & Abstract Factory Pattern

- A component responsible solely for the wholesale (not piecewise) creation of objects.

## Motivation

- somtimes your object creation logic becomes too convoluted
  - simple initializer is not problem, but your initializer get longer and longer and more sophisticated
- initializer is not descriptive
  - name is always "\_\_init\_\_"
  - cannot overload initializer with different name
  - can turn into 'optional parameter hell'
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to

  - single statement that would create an object
  - 객체의 생성을 아웃소싱하는 것
  - 방식
    - A separate method (Factory Method)
      - typically static method
    - That may exist in a separate class (Factory)
      - charge of manufacturing different types of objects
    - can create hierarchy of factories with abstract factory

- 즉, 여러 유형의 객체를 복잡한 생성자를 통해서 생성해야 할 때, 인자로 무엇을 넘겨줄지 클라이언트에게 고민하게 만들지말고, 스태틱 메소드(=팩토리메소드)를 호출해서 생성을 일임하자. (생성자는 descriptive 하지 않기 때문에 enduser는 잘 모른다)
- 타입의 계층을 가지고 있다면, 팩토리의 계층을 가질 수 있다.

## Summary

- A factory method is a static method that creates objects
- A factory is any entity that can take care of object creation
- A factory can be external or reside inside the object as an inner class
- Hierarchies of factories can be used to create related objects
