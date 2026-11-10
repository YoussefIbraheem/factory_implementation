import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def __deepcopy__(self, memo=None):
        
        if memo is None:
            memo = {}
            
        new = self.__class__.__new__(self.__class__)
        memo[id(self)] = new
        new.x = copy.deepcopy(self.x, memo)
        new.y = copy.deepcopy(self.y, memo)
        new.color = copy.deepcopy(self.color, memo)
        
        return new


    def move(self, x, y):
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color

    def clone(self):
        return copy.deepcopy(self)


class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius

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
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height

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
