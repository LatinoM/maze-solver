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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
            # otherwise, Pick a random neighbour
            next_cell_coords = random.choice(to_visit)
            next_cell = self._cells[next_cell_coords[0]][next_cell_coords[1]]

            # break down the walls between cells
            if next_cell_coords[0] < i: # above
                #print("Moving to cell above")
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_cell_coords[0] > i: # below
                #print("Moving to cell below")
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_cell_coords[1] < j: # to left
                #print("Moving to cell to left")
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            else: # to right
                #print("Moving to cell to right")
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            # Move to that cell
            self._break_walls_r(next_cell_coords[0], next_cell_coords[1])


    def _get_adjacent(self, i, j):
        adjacent = []
        
        if i-1 >= 0:
            adjacent = self._add_if_not_visted(adjacent, i-1, j) # up
        if i+1 < self.num_rows:
            adjacent = self._add_if_not_visted(adjacent, i+1, j) # down
        if j-1 >= 0:
            adjacent = self._add_if_not_visted(adjacent, i, j-1) # left
        if j+1 < self.num_cols:
            adjacent = self._add_if_not_visted(adjacent, i, j+1) # right
        return adjacent
    
    def _add_if_not_visted(self, adjacent_list, i, j):
        output = adjacent_list.copy()
        if not self._cells[i][j].visited:
            output.append((i, j))
        return output
    
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        print(f"solving {i}, {j}")
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        neighbours = self._get_adjacent(i, j)
        #print(neighbours)
        for cell in neighbours:
            print(f"checking if {cell} can be moved to")
            if self._can_move(i, j, cell[0], cell[1]):
                self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]])
                if self._solve_r(cell[0], cell[1]):
                    return True
                self._cells[i][j].draw_move(self._cells[cell[0]][cell[1]], True)
        return False

    def _can_move(self, start_i, start_j, next_i, next_j):
        if start_i < next_i: # down
            return not self._cells[start_i][start_j].has_bottom_wall
        if start_i > next_i: # up
            return not self._cells[start_i][start_j].has_top_wall
        if start_j < next_j: # right
            return not self._cells[start_i][start_j].has_right_wall
        return not self._cells[start_i][start_j].has_left_wall
            
        


            


        