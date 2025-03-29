import pyxel
from square import Square
from square import SquareState
import math

class Grid:
    def __init__(self, square_size, height, width, x_pix_offset_left, x_pix_offset_right, y_pix_offset_top, y_pix_offset_bot):
        self.height = height # in terms of grid spaces
        self.width = width
        
        self.square_size = square_size  # N for NxN pixel size of a square
        self.pix_height = height * square_size
        self.pix_width = width *  square_size
        
        self.x_pix_offset_left = x_pix_offset_left
        self.x_pix_offset_right = x_pix_offset_right
        self.y_pix_offset_bot = y_pix_offset_bot
        self.y_pix_offset_top = y_pix_offset_top
        
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
    
    #return tuple of x and y on grid coordinates corresponding to pixel x,y
    def _pix_to_grid_space(self, pix_x, pix_y):
        # check pixel is within the grid
        if (pix_x >= self.x_pix_offset_left and pix_x <= self.x_pix_offset_right and pix_y >= self.y_pix_offset_bot and pix_y <= self.y_pix_offset_top):
            grid_x = math.ceil((pix_x - self.x_pix_offset_left) / self.square_size)
            grid_y = math.floor((pix_y + self.y_pix_offset_bot) / self.square_size)
            return (grid_x, grid_y)
        else:
            print("ERROR: Specified pixel is not within the grid.")
            return None
        
    # returns None if pixel is unoccupied by a Square, else returns a Square
    def get_square(self, pix_x, pix_y):
        pass