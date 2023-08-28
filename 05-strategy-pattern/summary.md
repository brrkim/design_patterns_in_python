System behavior partially specified at runtime.

Making Tea decompose into higher and lower level part algorithm
- making hot beverage (boil water, pour into cup) --> high level
- tea specific things (put teabag into water) --> low level

high level algorithm can then be reused for making coffee or hot chocoate
- supported by beverage specific strategies

Strategy | (basically) Enables the exact 'behavior' of a system to be selected 'at run-time'

런타임에 실제 동작을 구체화하기 때문에, 실제 동작을 어떤 컴포넌트이던간에 멕일 수 있고
컴포넌트는 로우 레벨 스트레티지로 하이 레벨 스트레티지를 재사용 가능

Well, the strategy is essentially a separate chunk of code, 
basically a blueprint for some sort of algorithm 
that you can subsequently use inside the object that consumes it.
So in this case, the text processor takes a particular list strategy.
And then in the append list, it actually uses this list strategy to perform operations on list elements.
So the flexibility here is that you can construct a brand new list strategy.
You can substitute this and put it in place of the list strategy already being used.


1) You define an algorithm at a high level, sort of very general, 
2) and then what you do is you define the interface that you expect each of the strategies to follow.
3) And subsequently you provide for the dynamic composition of these strategies.
So you make the strategies and then you enable the composition of those strategies in the resulting