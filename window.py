from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        
        self.canvas = Canvas(width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
