from window import Window
from point import Point
from line import Line

class Cell():
    def __init__(self, x1, y1, x2, y2, window=None, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.__x1 = x1 # left
        self.__y1 = y1 # top
        self.__x2 = x2 # right
        self.__y2 = y2 # bottom
        self.__win = window

    def draw(self):
        if self.__win is None:
            return
        
        color = ""
        if self.has_left_wall:
            color = "green"
        else:
            color = "white"
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), color)
            
            
        if self.has_right_wall:
            color = "green"
        else:
            color = "white"
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), color)

        if self.has_top_wall:
            color = "green"
        else:
            color = "white"
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), color)

        if self.has_bottom_wall:
            color = "green"
        else:
            color = "white"
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), color)

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        color = ""
        if undo:
            color = "gray"
        else:
            color = "red"

        self.__win.draw_line(Line(self.get_center(), to_cell.get_center()), color)

    def get_center(self):
        # Returns point representing center
        x = ((self.__x2 - self.__x1) // 2) + self.__x1
        y = ((self.__y2 - self.__y1) // 2) + self.__y1
        return Point(x, y)
    
    def set_top_left(self, x, y):
        self.__x1 = x
        self.__y1 = y

    def set_bottom_right(self, x, y):
        self.__x2 = x
        self.__y2 = y

        
        

        
    
