from figure import Geom
from collor import ColorFig
from prettytable import PrettyTable
from math import pi
class Circle(Geom):
    name = "круг"
    def __init__(self, radius, color):
        self.__radius = radius
        a = ColorFig()
        a.color = color
        self.__color = a.color
    def get_area(self):
        return 2 * pi * (self.__radius ** 2)
    def repr(self):
        table = PrettyTable()
        table.field_names = ["фигура", "цвет", "площадь"]
        table.add_row([self.name, self.__color, self.get_area()])
        print(table)
