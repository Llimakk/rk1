from figure import Geom
from collor import ColorFig
from prettytable import PrettyTable

class Square(Geom):

    name = "квадрат"

    def __init__(self, height, color):
        self.__height = height
        a = ColorFig()
        a.color = color
        self.__color = a.color

    def get_area(self):
        return self.__height ** 2

    def repr(self):
        table = PrettyTable()
        table.field_names = ["фигура", "цвет", "площадь"]
        table.add_row([self.name, self.__color, self.get_area()])
        print(table)
