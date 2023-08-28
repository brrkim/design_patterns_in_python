- Iteration is a core functionality of various data structures.
- An 'iterator' is a class that facilitates the traversal.
  - iterator keeps a reference to the current element
  - knows how to move to a different element
- iterator protocol requires 2 things
  1. if you want an object to be iterable, it has iter method (**iter**()) to expose the iterator
  2. iterator has to have a next method (**next()**) to return each of the iterated elements or raise StopIteration when it's done
- Iterator: An object that facilitates the traversal of a data structure.

- Summary
  - iterator specifies how you can traverse a particular object and stateful interators
  - problem) stateful iterators cannot be recursive
    - you always can navigate from current state to next state
  - solution) yield allows for much more succinct iteration of iteration process
