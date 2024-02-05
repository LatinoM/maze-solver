from cell import Cell
from point import Point
from line import Line
from window import Window
from line_helper import get_line

def main():
    win = Window(800, 600)
    c1 = Cell(100, 100, 110, 110, win, left=False)
    c1.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()