import time
import random
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
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            self._seed = random.seed(seed)
        self._cells = []
        self._create_cells()
        if len(self._cells)==0:
            raise IndexError("maze size is zero")
        self._break_entrance_and_exit()
        start_i = random.choice(range(self.num_rows))
        start_j = random.choice(range(self.num_cols))
        self._break_walls_r(start_i, start_j)

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

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0] 
        end_cell = self._cells[-1][-1]
        start_cell.has_left_wall = False
        start_cell.has_right_wall = False
        start_cell.has_top_wall = False
        start_cell.has_bottom_wall = False
        start_cell.draw()
        end_cell.has_left_wall = False
        end_cell.has_right_wall = False
        end_cell.has_top_wall = False
        end_cell.has_bottom_wall = False
        end_cell.draw()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = self._get_adjacent(i, j)
            if len(to_visit) == 0:
                current_cell.draw()
                return
            next_cell_coords = random.choice(to_visit)
            next_cell = self._cells[next_cell_coords[0]][next_cell_coords[1]]
            if next_cell_coords[0] < i: # above
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_cell_coords[0] > i: # below
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_cell_coords[1] < j: # to left
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            else: # to right
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            self._break_walls_r(next_cell_coords[0], next_cell_coords[1])


    def _get_adjacent(self, i, j):
        adjacent = []
        for x in [-1, 1]:
            for y in [-1, 1]:
                after_left = j+x >= 0
                before_right = j+x < self.num_cols
                below_top = i+y >= 0
                above_bottom = i+y < self.num_rows
                if after_left and before_right and above_bottom and below_top:
                    if not self._cells[i+y][j+x].visited:
                        adjacent.append((i+y, j+x))
        return adjacent
        


            


        