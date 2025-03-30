import pyxel
import random
from square import Square
from square import SquareState
from block import Block
import math

class Grid:
    block_list = random.choices(range(1, 8), k=500) # generate 500 random block types

    def __init__(self, square_size, height, width, x_pix_offset_left, y_pix_offset_top, y_pix_offset_bot):
        self.height = height # in terms of grid spaces
        self.width = width
        
        self.square_size = square_size  # N for NxN pixel size of a square
        self.pix_height = height * square_size
        self.pix_width = width *  square_size
        
        self.x_pix_offset_left = x_pix_offset_left
        self.y_pix_offset_bot = y_pix_offset_bot
        self.y_pix_offset_top = y_pix_offset_top
        
        self.grid = [[]]
        self.init_grid()
    
    def init_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = None
        
    def get_grid(self):
        return self.grid
    
    def destroy_square(self, x, y):
        self.grid[x][y] = None

    def spawn_block(self, index):
        Block(Grid.block_list[index], (self.width / 2, self.height - 1), 0, self)
    
    def reinforce_squares(self, x):
        for square in self.grid()[x]:
            square.set_state(SquareState.INVINCIBLE)
    
    def has_live(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].get_state() == SquareState.LIVE:
                    return True
        return False
    
    def check_win(self, win_height):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].get_state() == SquareState.SET:
                    if i + 1 >= win_height:
                        return True
        return False

    #return tuple of x and y on grid coordinates corresponding to pixel x,y
    def _pix_to_grid_space(self, pix_x, pix_y):
        # check pixel is within the grid
        if (pix_x >= self.x_pix_offset_left and pix_x <= self.x_pix_offset_left + self.pix_width and pix_y >= self.y_pix_offset_bot and pix_y <= self.y_pix_offset_top):
            grid_x = math.floor((pix_x - self.x_pix_offset_left) / self.square_size)
            grid_y = math.floor((pix_y - self.y_pix_offset_bot) / self.square_size)
            return (grid_x, grid_y)
        else:
            print("ERROR: Specified pixel is not within the grid.")
            return None
        
    # returns None if pixel is unoccupied by a Square, else returns a Square
    def get_square(self, pix_x, pix_y):
        x, y = self._pix_to_grid_space(pix_x, pix_y)
        return self.grid[x][y]