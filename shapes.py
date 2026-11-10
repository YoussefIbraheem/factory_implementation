import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = "black"

    @abstractmethod
    def __deepcopy__(self, memo=None):

        new = self.__class__()
        new.__dict__.update(self.__dict__)

        return new

    @abstractmethod
    def configure(self, **kwargs):
        self.x = kwargs.get("x", self.x)
        self.y = kwargs.get("y", self.y)
        self.color = kwargs.get("color", self.color)

    def clone(self):
        return copy.deepcopy(self)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def configure(self, **kwargs):
        super().configure(**kwargs)
        self.radius = kwargs.get("radius", self.radius)

    def __str__(self):
        return f"""
                X Axis: {self.x}
                Y Axis: {self.y}
                Color: {self.color}
                Circle Radius: {self.radius}
                """

    def __deepcopy__(self, memo=None):
        new = super().__deepcopy__(memo)
        new.radius = copy.deepcopy(self.radius, memo)
        return new


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def configure(self, **kwargs):
        super().configure(**kwargs)
        self.width = kwargs.get("width", self.width)
        self.height = kwargs.get("height", self.height)

    def __str__(self):
        return f"""
                X Axis: {self.x}
                Y Axis: {self.y}
                Color: {self.color}
                Rectangle Width: {self.width}
                Rectangle Height: {self.height}"""

    def __deepcopy__(self, memo=None):
        new = super().__deepcopy__(memo)
        new.width = copy.deepcopy(self.width, memo)
        new.height = copy.deepcopy(self.height, memo)
        return new
