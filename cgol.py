import math
import random

class Grid:
    """
        Create a new grid:

            Grid()

        Create a grid and initialize with data:

            Grid(
                [
                    [0, 1],
                    [1, 1]
                ]
            )

    """
    def __init__(self, init=None):
        self.gridata = {}
        if init:
            for y, row in enumerate(init):
                for x, val in enumerate(row):
                    if val == 1:
                        self.set(x, y, 1)

    def __eq__(self, other):
        return self.gridata == other.gridata

    def get(self, x, y):
        """
          This function returns the value of
          one specific cell.
        """
        if (x, y) in self.gridata:
            return self.gridata[(x, y)]
        elif not (x, y) in self.gridata:
            return 0

    def set(self, x, y, value):
        """
          one specific cell.
        """
        self.gridata[(x, y)] = value

    def check_cell(self, x, y, dim):
        if x < 0:
            return 0
        elif y < 0:
            return 0
        elif x > dim - 1:
            return 0
        elif y > dim - 1:
            return 0
        else:
            return self.get(x, y)

    def count_neighbours(self, x, y, dim):
        """
          This funciton counts all alive cells
          surrounding one specific cell.
        """
        count = 0

        if self.check_cell(x-1, y-1, dim) > 0:
            count += 1

        if self.check_cell(x, y-1, dim) > 0:
            count += 1

        if self.check_cell(x+1, y-1, dim) > 0:
            count += 1

        if self.check_cell(x-1, y, dim) > 0:
            count += 1

        if self.check_cell(x+1, y, dim) > 0:
            count += 1

        if self.check_cell(x-1, y+1, dim) > 0:
            count += 1

        if self.check_cell(x, y+1, dim) > 0:
            count += 1

        if self.check_cell(x+1, y+1, dim) > 0:
            count += 1

        return count

    def ccoords(self, m_pos, cell_w):
        x = math.floor(m_pos[0]/cell_w)
        y = math.floor(m_pos[1]/cell_w)
        return (x, y)

    def live_cells(self, grid):
        return self.gridata.keys()

    def insert(self, x, y, newg):
        pos = newg.live_cells(newg)
        for i in pos:
            self.set(i[0] + x, i[1] + y, 1)

    def random(self, dim, prob):
        for i in range(dim):
            for j in range(dim):
                v = random.randrange(0,100)
                if v <= prob:
                    self.set(i, j, 1)
                else:
                    self.set(i, j, 0)

    def clear(self):
        self.gridata.clear()


"""
The View class handles the view regarding zoom and pan
"""


class View:

    """
    The View class handles the view regarding zoom and pan
    """
    def __init__(self, view_size, x, y):
        self.view_size = view_size
        self.x = x
        self.y = y

    def pan(self, grid_size, x, y):
        self.x = max(min(self.x + x, grid_size-self.view_size), 0)
        self.y = max(min(self.y + y, grid_size-self.view_size), 0)

    def zoom(self, grid_size, f):
        self.view_size = math.ceil(max(min(self.view_size * f, grid_size), 1))
        if self.view_size + self.x > grid_size:
            self.pan(grid_size, grid_size - (self.view_size + self.x), 0)
        if self.view_size + self.y > grid_size:
            self.pan(grid_size, 0, grid_size - (self.view_size + self.y))


def conwayslife(g, dim):
    newgrid = Grid()

    for x in range(dim):
        for y in range(dim):
            count = g.count_neighbours(x, y, dim)
            if count < 2:
                newgrid.set(x, y, 0)
            if count == 2 and g.get(x, y) == 1:
                newgrid.set(x, y, 1)
            if count == 3:
                newgrid.set(x, y, 1)
            if count > 3:
                newgrid.set(x, y, 0)

    return newgrid
