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


# Step3 : Create a factory to generate objects of concrete Class
class ShapeFactory:
    """ You use @staticmethod to define a method that belongs to the class itself,
     not any specific instance. It doesn't access or modify instance (self) or class (cls) data and is used for utility
     functions that are logically related to the class but don't require an instance to work. """
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "CIRCLE":
            return Circle()
        elif shape_type == "RECTANGLE":
            return Rectangle()
        elif shape_type == "SQUARE":
            return Square()
        else:
            return None


# Step4 :Use the Factory to get object of concrete Class
class FactoryPattern:
    @staticmethod
    def main():
        # Create the Factory
        shape_factory = ShapeFactory()
        # get an object of Circle and call it Draw method
        shape1 = shape_factory.get_shape("CIRCLE")
        print(shape1.draw())

        # Get an object of Rectangle and call it Draw method
        shape2 = shape_factory.get_shape("RECTANGLE")
        print(shape2.draw())

        # Get an object of Square and call it Draw method
        shape3 = shape_factory.get_shape("SQUARE")
        print(shape3.draw())


# Ste5 : Verify the Output

if __name__ == "__main__":
    FactoryPattern.main()
