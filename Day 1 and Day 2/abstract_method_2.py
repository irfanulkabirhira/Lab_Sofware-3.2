from abc import ABC, abstractmethod


# Step 1: Create an interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Step 2: Create concrete classes implementing the same interface
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"


class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


# Step 3: Use the concrete classes
def main():
    # Create objects of the concrete classes
    shapes = [Rectangle(), Square(), Circle()]

    # Iterate and call the draw method for each shape
    for shape in shapes:
        print(shape.draw())


# Entry point of the program
if __name__ == "__main__":
    main()
