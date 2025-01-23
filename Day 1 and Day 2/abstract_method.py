from abc import ABC, abstractmethod

# step1 : Create an interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# step2 : Create a concrete class Implementing the same interface
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"
class Square(Shape):
    def draw(self):
        return "Drawing a square"
class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

# Execution code directly written at the root level
rectangle = Rectangle()
square = Square()
circle = Circle()

print(rectangle.draw())
print(square.draw())
print(circle.draw())