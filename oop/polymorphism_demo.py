# polymorphism_demo.py

import math

class Shape:
    """
    Base class representing a generic shape.
    """
    def area(self):
        """
        Method to calculate the area of the shape.
        Must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        Formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
