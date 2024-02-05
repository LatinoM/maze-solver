from line_helper import get_line
from window import Window

class Cell():
    def __init__(self, x1, y1, x2, y2, window, left=True, right=True, top=True, bottom=True):
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
        if self.has_left_wall:
            self.__win.draw_line(get_line(self.__x1, self.__y1, self.__x1, self.__y2), "green")
            
        if self.has_right_wall:
            self.__win.draw_line(get_line(self.__x2, self.__y1, self.__x2, self.__y2), "green")

        if self.has_top_wall:
            self.__win.draw_line(get_line(self.__x1, self.__y1, self.__x2, self.__y1), "green")

        if self.has_bottom_wall:
            self.__win.draw_line(get_line(self.__x1, self.__y2, self.__x2, self.__y2), "green")

        
        

        
    
