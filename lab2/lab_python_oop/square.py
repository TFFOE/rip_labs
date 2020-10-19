from lab_python_oop.rectangle import Rectangle
from lab_python_oop.figure_color import Color

class Square(Rectangle):
    figureType = "Квадрат"

    @classmethod
    def getFigureType(cls):
        return cls.figureType

    def __init__ (self, sideLength, colorName):
        self._color = Color(colorName)
        super().__init__(sideLength, sideLength, colorName)

    def __repr__(self):
        return f"{Square.getFigureType()} {self._color.colorValue} цвета со стороной {self._width}."
    pass
    