import pyxel
from square import Square
from square import SquareState


class Grid:
    def __init__(self, square_size, height, width, x_offset, y_offset):
        self.square_size = square_size  # N for NxN pixel size of a square
        self.height = height
        self.width = width
        self.pix_height = height * square_size
        self.pix_width = width *  square_size
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.grid = [[]]
        self.init_grid()
    
    def init_grid(self):
        for i in self.height:
            for j in self.width:
                self.grid[i][j] = None
        
    def get_grid(self):
        return self.grid
    
    def destroy_square(self, x, y):
        self.grid[x][y] = None
        
    def spawn_block(self):
        pass
    
    def reinforce_squares(self, x):
        for square in self.grid()[x]:
            square.set_state(SquareState.INVINCIBLE)
    
    # returns None if grid coordinate is unoccupied by a Square, else returns a Square
    def get_square(self, x, y):
        pass

    # returns None if pixel is unoccupied by a Square, else returns a Square
    def get_square(self, pix_x, pix_y):
        pass