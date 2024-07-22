from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        else: 
            raise StopIteration
        
    def __iter__(self):
        return self
    
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self._items)
    
    def __iter__(self):
        return self.create_iterator()
    
if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    for item in iterator:
        print(item)

