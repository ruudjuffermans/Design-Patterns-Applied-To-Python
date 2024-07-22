from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"ConcretePrototype(name={self.name}, data={self.data})"
    
if __name__ == "__main__":
    prototype = ConcretePrototype("Prototype1", [1,2,3])

    cloned_obj = prototype.clone()

    print(prototype)
    print(cloned_obj)

    cloned_obj.data.append(4)
    print(prototype)
    print(cloned_obj)