import cgol


def read_plaintext(s):
    """
    Read a plaintext definition, and return a Grid object.
    """
    # Read line by line and calculate the width and height
    # Create a new grid object and set the cells that are on
    # Return the new grid
    yoffset = 0
    grid = cgol.Grid()

    for i in s.splitlines():
        i = i.strip()
        if not i:
            pass
        elif i[0] == "!":
            pass
        else:
            for x, val in enumerate(i):
                if val == "O":
                    grid.set(x, yoffset, 1)
            yoffset += 1
    return grid


def export_plaintext(g):
    """
    Takes a grid, calculiates the plaintext representation and returns it as a string.
    """
    pass


class Grid:
    def place(self, x, y, g):
        """
        Place a grid at position x, y within this grid, erasing the data that's already there.
        """
        pass

    def place_center(self, g):
        """
        Place a grid in the center of this grid.
        """
        pass
