from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from numpy import euler_gamma


if (__name__ == "__main__"):
    rectangle = Rectangle(10, 20, "фиолетового")
    square = Square(10, "чёрного")
    circle = Circle(5, "красного")

    print (rectangle)
    print (square)
    print (circle)
    print ("Euler gamma constant y = {}".format(euler_gamma))