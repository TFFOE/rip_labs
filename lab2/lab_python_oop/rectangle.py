from lab_python_oop.figure import Figure
from lab_python_oop.figure_color import Color

class Rectangle(Figure):
    figureType = "Прямоугольник"

    @classmethod
    def getFigureType(cls):
        return cls.figureType

    def __init__(self, width, height, colorName):
        self._width = width
        self._height = height
        self._color = Color(colorName)

    def square(self):
        return self._width * self._height

    def __repr__(self):
        return f"{Rectangle.getFigureType()} {self._color.colorValue} цвета шириной {self._width} и высотой {self._height}."