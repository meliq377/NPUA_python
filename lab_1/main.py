class Shape:
    def area(self):
        pass

    def volume(self):
        pass


class TwoDimensional(Shape):
    pass


class ThreeDimensional(Shape):
    pass


class Square(TwoDimensional):
    def area(self, side):
        return side * side


class Triangle(TwoDimensional):
    def area(self, base, height):
        return 0.5 * base * height


class Cube(ThreeDimensional):
    def volume(self, side):
        return side * side * side


class Cone(ThreeDimensional):
    def volume(self, radius, height):
        return (1/3) * 3.14 * radius * radius * height


