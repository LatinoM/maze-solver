from cell import Cell
from point import Point
from line import Line
from window import Window

def main():
    win = Window(800, 600)
    c1 = Cell(100, 100, 110, 110, win, right=False)
    c2 = Cell(110, 100, 120, 110, win, left=False)
    c1.draw()
    c2.draw()
    c1.draw_move(c2)
    win.wait_for_close()

if __name__ == "__main__":
    main()