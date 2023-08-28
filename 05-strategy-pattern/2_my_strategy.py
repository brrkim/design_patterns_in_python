from abc import *

class ListStrategy(metaclass=ABCMeta):
    @abstractmethod
    def start(self, buffer): pass
    @abstractmethod
    def end(self, buffer): pass
    @abstractmethod
    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')
    def end(self, buffer):
        buffer.append('</ul>\n')
    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class TextProcessor:
    list_strategy: ListStrategy
    def __init__(self):
        self.buffer = []
        
    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(
                self.buffer, item
            )
        self.list_strategy.end(self.buffer)
    
    def set_list(self, ls:ListStrategy):
        self.list_strategy = ls

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']

    tp = TextProcessor()
    
    tp.set_list(MarkdownListStrategy())
    tp.append_list(items)
    print(tp)
    
    tp.clear()
    
    tp.set_list(HtmlListStrategy())
    tp.append_list(items)
    print(tp)