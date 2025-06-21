import math

class Shape:
    """
    Base class for geometric shapes, demonstrating the concept of a placeholder
    method that must be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        Raises:
            NotImplementedError: If the method is not overridden in a derived class.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inheriting from Shape.
    Overrides the area() method to calculate the rectangle's area.
    """
    def __init__(self, length, width):
        """
        Initializes a new Rectangle instance.
        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            float or int: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inheriting from Shape.
    Overrides the area() method to calculate the circle's area.
    """
    def __init__(self, radius):
        """
        Initializes a new Circle instance.
        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle using the formula pi * radius^2.
        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
