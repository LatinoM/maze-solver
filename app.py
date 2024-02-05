from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    p1 = Point(100, 60)
    p2 = Point(650, 450)
    l1 = Line(p1, p2)
    win.draw_line(l1, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()