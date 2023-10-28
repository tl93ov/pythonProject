class Polygon:
    def __init__(self, sides, color='piros'):
        self.sides = sides
        self.color = color
        self.oldalszelszelesseg = 2


class Triangle:
    pass

my_polygon = Polygon(sides=4, color='kék')

print(f"ennek a polygonnak {my_polygon.sides} oldala van és {my_polygon.color} színű és oldalszélessége {my_polygon.oldalszelszelesseg}")

my_triangle = Polygon(3)


print(f"ennek a polygonnak {my_triangle.sides} oldala van és {my_triangle.color} színű és oldalszélessége {my_triangle.oldalszelszelesseg}")
