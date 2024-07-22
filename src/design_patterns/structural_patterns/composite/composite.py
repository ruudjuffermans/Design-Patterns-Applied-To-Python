from abc import ABC, abstractmethod

class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Graphic):
    def draw(self):
        return 'Circle'
    
class Rectangle(Graphic):
    def draw(self):
        return 'Rectangle'
    

class CompositeGraphic(Graphic):
    def __init__(self):
        self._graphics = []

    def add(self, graphic):
        self._graphics.append(graphic)

    def remove(self, graphic):
        self._graphics.remove(graphic)

    def draw(self):
        results = []
        for graphic in self._graphics:
            results.append(graphic.draw())
        return " + ".join(results)
    
if __name__ == "__main__":
    circle1 = Circle()
    circle2 = Circle()

    rectangle = Rectangle()

    composite1 = CompositeGraphic()
    composite1.add(circle1)
    composite1.add(rectangle)

    composite2 = CompositeGraphic()
    composite2.add(composite1)
    composite2.add(rectangle)

    print("Composite 1 drawing: " + composite1.draw())
    print("Composite 2 drawing: " + composite2.draw())
        