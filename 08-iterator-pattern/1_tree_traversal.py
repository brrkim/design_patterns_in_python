class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  ## iter method which has to return some sort of iterator
  ## iterator has to implement next method to move from one element to another
  def __iter__(self):
    return InOrderIterator(self)

## terrible, stateful iteration --> SRP Problem
class InOrderIterator:
  def __init__(self, root):
    self.root = self.current = root
    self.yielded_start = False
    while self.current.left:
      self.current = self.current.left

  def __next__(self):
    if not self.yielded_start:
      self.yielded_start = True
      return self.current

    if self.current.right:
      self.current = self.current.right
      while self.current.left:
        self.current = self.current.left
      return self.current
    else:
      p = self.current.parent
      while p and self.current == p.right:
        self.current = p
        p = p.parent
      self.current = p
      if self.current:
        return self.current
      else:
        raise StopIteration

# nicer iteration mechanic.
# use yield keyword! - yield 키워드를 사용하면 stateful 하게 관리할 필요가 없어짐
# (yield 자체가 iterator로 반환하고 즉시 종료하는게 아니라 다음까지 대기함)
# yield the elements as we encounter them 
# and we sort of make the state or position implicit as opposed to explicit.
# we don't have to micromanage state of iterator
def traverse_in_order(root):
  def traverse(current):
    if current.left:
      for left in traverse(current.left):
        yield left
    yield current
    if current.right:
      for right in traverse(current.right):
        yield right
  for node in traverse(root):
    yield node



if __name__ == '__main__':
  #   1
  #  / \
  # 2   3

  # in-order: 213
  # preorder: 123
  # postorder: 231

  root = Node(1,
              Node(2),
              Node(3))

  it = iter(root)

  # print([next(it).value for x in range(3)])

  # for x in root:
  #   print(x.value)

  for y in traverse_in_order(root):
    print(y.value)