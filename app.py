from cell import Cell
from point import Point
from line import Line
from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 11, 15, 50, 50, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()