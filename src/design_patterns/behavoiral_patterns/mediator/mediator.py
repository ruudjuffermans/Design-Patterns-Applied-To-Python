from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self._component1 = None
        self._component2 = None

    def set_component1(self, component):
        self._component1 = component
        self._component1.set_mediator(self)

    def set_component2(self, component):
        self._component2 = component
        self._component2.set_mediator(self)

    def notify(self, sender, event):
        if event == "A":
            print("Mediator handles A: triggers component 2")
            self._component2.do_action()
        elif event == "B":
            print("Mediator handles B: triggers component 1")
            self._component1.do_action()

class BaseComponent(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do(self):
        print("Component 1 does A.")
        self._mediator.notify(self, "A")

    def do_action(self):
        print("Component 1 does its own action.")

class Component2(BaseComponent):
    def do(self):
        print("Component 2 does B.")
        self._mediator.notify(self, "B")

    def do_action(self):
        print("Component 2 does its own action.")

if __name__ == "__main__":
    mediator = ConcreteMediator()

    c1 = Component1()
    c2 = Component2()

    mediator.set_component1(c1)
    mediator.set_component2(c2)

    print("Client triggers Component 1")
    c1.do()
    print("Client triggers Component 2")
    c2.do()
