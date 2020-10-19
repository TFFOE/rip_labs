from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from numpy import euler_gamma


if (__name__ == "__main__"):
    rectangle = Rectangle(3, 3, "синего")
    circle = Circle(3, "зелёного")
    square = Square(3, "красного")

    print (rectangle)
    print (square)
    print (circle)
    print ("Euler gamma constant y = {}".format(euler_gamma))