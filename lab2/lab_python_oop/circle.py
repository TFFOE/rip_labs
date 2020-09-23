from lab_python_oop.figure import Figure
from lab_python_oop.figure_color import Color
from math import pi

class Circle(Figure):
    figureType = "Круг"

    def __init__(self, radius, colorName):
        self._radius = radius
        self._color = Color(colorName)
    def square(self):
        return pi * self._radius ** 2

    def __repr__(self):
        return f"{self.figureType} {self._color.colorValue} цвета радиусом {self._radius}."