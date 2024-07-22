from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"
    
class Decorator(Component):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def operation(self):
        return self._component.operation()
    

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreateDecoratorA({self._component.operation()})"
    
class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreateDecoratorB({self._component.operation()})"
    
if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: ive got a simple component:")
    print(f"RESULT: {simple.operation()}")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: ive now got a decorated component:")
    print(f"RESULT: {decorator2.operation()}")