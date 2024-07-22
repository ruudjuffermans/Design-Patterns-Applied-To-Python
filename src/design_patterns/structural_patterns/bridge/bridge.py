from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

class BlueColor(Color):
    def apply_color(self):
        return 'blue'
    
class RedColor(Color):
    def apply_color(self):
        return 'red'
    
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Circle drawn in {self.color.apply_color()} color"
    
class Square(Shape):
    def draw(self):
        return f"Square drawn in {self.color.apply_color()} color"
    
if __name__ == '__main__':
    blue = BlueColor()
    red = RedColor()

    circle = Circle(blue)
    square = Square(red)

    print(circle.draw())
    print(square.draw())