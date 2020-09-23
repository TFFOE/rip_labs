from lab_python_oop.rectangle import Rectangle
from lab_python_oop.figure_color import Color

class Square(Rectangle):
    figureType = "Квадрат"

    def __init__ (self, sideLength, colorName):
        self._color = Color(colorName)
        self._width = sideLength
        self._height = sideLength

    def __repr__(self):
        return f"{self.figureType} {self._color.colorValue} цвета со стороной {self._width}."
    pass
    