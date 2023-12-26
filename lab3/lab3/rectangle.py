from figure import Geom
from collor import ColorFig
from prettytable import PrettyTable
class Rectangle(Geom):

    name = "прямоугольник"

    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        a = ColorFig()
        a.color = color
        self.__color = a.color

    def get_area(self):
        return self.__width * self.__height

    def repr(self):
        table = PrettyTable()
        table.field_names = ["фигура", "цвет", "площадь"]
        table.add_row([self.name, self.__color, self.get_area()])
        print(table)
