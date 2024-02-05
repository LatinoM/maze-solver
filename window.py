from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        
        self.canvas = Canvas()
        self.canvas.pack()

        self.running = False