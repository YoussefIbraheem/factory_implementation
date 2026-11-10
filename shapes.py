import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    
    def __init__(self,x: int = 0, y: int = 0, color: str = "black"):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def __deepcopy__(self):
        x = copy.deepcopy(self.x)
        y = copy.deepcopy(self.y)
        color = copy.deepcopy(self.color)

        new = self.__class__(x, y, color)

        new.__dict__.update(self.__dict__)

        return new


class Circle(Shape):
    def __init__(self, radius: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius

    def __str__(self):
        return f"Circle Radius: {self.radius}"
    
    def __deepcopy__(self):
        new = super().__deepcopy__()
        new.radius = copy.deepcopy(self.radius)
        return new
    
class Rectangle(Shape):
    def __init__(self, width: int, height: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle Width: {self.width}, Height: {self.height}"

    def __deepcopy__(self):
        new = super().__deepcopy__()
        new.width = copy.deepcopy(self.width)
        new.height = copy.deepcopy(self.height)
        return new

