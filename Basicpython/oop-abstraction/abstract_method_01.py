from abc import ABC, abstractmethod

from cryptography.hazmat.primitives.ciphers import aead


class Shape(ABC):

    def execute(self):
        print("Calculating area...")
        self.area()

    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"Area of Rectangle: {area}")

#
# # Example usage
r = Rectangle(5, 10)
r.execute()
# # Polymorphism: Shape type reference holding Rectangle object
# shape: Shape = Rectangle(5, 10)
# shape.execute()
