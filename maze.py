import time
from cell import Cell
class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = [Cell(0,0,0,0, self._win) for _ in range(self.num_cols)]
            self._cells.append(row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cells(i, j)
    
    def _draw_cells(self, i, j):
        current_cell = self._cells[i][j]

        # left x = maze x + (cell_width * j)
        xl = self.x1 + (self.cell_size_x * j)
        # right x = maze x + (cell_width * (j+1))
        xr = self.x1 + (self.cell_size_x * (j+1))
        # top y = maze y + (cell_height * i)
        yt = self.y1 + (self.cell_size_y * i)
        # bottom y = maze y + (cell_height * (i+1))
        yb = self.y1 + (self.cell_size_y * (i+1))
        current_cell.set_top_left(xl, yt)
        current_cell.set_bottom_right(xr, yb)
        current_cell.draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

        