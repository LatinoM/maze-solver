import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_creates_size_zero(self):
        num_cols = 0
        num_rows = 0
        def create_empty_maze():
            return Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertRaises(
            IndexError,
            create_empty_maze
        )
        
    def test_entrance_and_exit_is_removed(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        start_cell=m1._cells[0][0]
        end_cell=m1._cells[-1][-1]
        self.assertEqual(
            (start_cell.has_left_wall,start_cell.has_right_wall,start_cell.has_top_wall,start_cell.has_bottom_wall),
            (False, False, False, False),
        )
        self.assertEqual(
            (end_cell.has_left_wall,end_cell.has_right_wall,end_cell.has_top_wall,end_cell.has_bottom_wall),
            (False, False, False, False),
        )


if __name__ == "__main__":
    unittest.main()