if __name__ == '__main__':
    from rectangle import Rectangle
    from circle import Circle
    from square import Square
    r = Rectangle(3, 4, "red")
    c = Circle(12, "green")
    s = Square(2, "blue")
    r.repr()
    c.repr()
    s.repr()
