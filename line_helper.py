from line import Line
from point import Point

def get_line(x1, y1, x2, y2):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    return Line(p1, p2)