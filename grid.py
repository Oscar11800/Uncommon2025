import pyxel


class Grid:
    def __init__(self, square_size, height, width):
        self.square_size = square_size  # N for NxN pixel size of a square
        self.height = height
        self.width = width
        self.pix_height = height * square_size
        self.grid = []
    
    def get_grid(self):
        return self.grid
        