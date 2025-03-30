import pyxel
from utils import calculate_adjacent_squares
from enum import Enum
from square_state import SquareState

class Colors(Enum):
    PLAYER_1_INNER = 5
    PLAYER_1_OUTER = 4
    PLAYER_2_INNER = 7
    PLAYER_2_OUTER = 6

# A square is always a unit size in terms of the grid
class Square:
    def __init__(self, x, y, pix_x, pix_y, size, player):
        # grid coordinates
        self.x = x
        self.y = y
        # pixel coordinates
        self.pix_x = pix_x
        self.pix_y = pix_y
        # pixel size
        self.size = size # size is in terms of pixels
        self.state = SquareState.LIVE
        self.player = player
        
    def draw_invincible(self, grid):
        COLOR_INNER = 2
        COLOR_OUTER = 1
        pyxel.rect(self.pix_x, self.pix_y, self.size, self.size, COLOR_INNER)
        if self.pix_x == 0:
            pyxel.rect(self.pix_x, self.pix_y, 1, self.size, COLOR_OUTER)
        if self.pix_x == len(grid[0]) - 1:
            pyxel.rect(self.pix_x + self.size - 1, self.pix_y, 1, self.size, COLOR_OUTER)
        if self.pix_y == len(grid) - 1:
            pyxel.rect(self.pix_x, self.pix_y, 1, self.size, COLOR_OUTER)
        else:
            square_above = grid[self.pix_x + 1][self.pix_y]
            if square_above is None or square_above.state != SquareState.INVINCIBLE:
                pyxel.rect(self.pix_x, self.pix_y, self.size, 1, COLOR_OUTER)
            else:
              print(square_above.state)
        
    def draw(self, grid):
        if self.state == SquareState.INVINCIBLE:
            return self.draw_invincible(grid)
        color = Colors.PLAYER_1_INNER.value if self.player == 1 else Colors.PLAYER_2_INNER.value
        pyxel.rect(self.pix_x, self.pix_y, self.size, self.size, color)
        # Calculate borders
        adjacent_squares = calculate_adjacent_squares(int(self.x), int(self.y), grid)
        border_color = Colors.PLAYER_1_OUTER.value if self.player == 1 else Colors.PLAYER_2_OUTER.value
        # Borders
        if not adjacent_squares[0]:
            pyxel.rect(self.pix_x, self.pix_y, self.size, 1, border_color)
        if not adjacent_squares[1]:
            pyxel.rect(self.pix_x, self.pix_y + self.size - 1, self.size, 1, border_color)
        if not adjacent_squares[2]:
            pyxel.rect(self.pix_x, self.pix_y, 1, self.size, border_color)
        if not adjacent_squares[3]:
            pyxel.rect(self.pix_x + self.size - 1, self.pix_y, 1, self.size, border_color)
            
        # Corners
        if adjacent_squares[0] and adjacent_squares[2]:
            pyxel.pset(self.pix_x, self.pix_y, border_color)
        if adjacent_squares[0] and adjacent_squares[3]:
            pyxel.pset(self.pix_x + self.size - 1, self.pix_y, border_color)
        if adjacent_squares[1] and adjacent_squares[2]:
            pyxel.pset(self.pix_x, self.pix_y + self.size - 1, border_color)
        if adjacent_squares[1] and adjacent_squares[3]:
            pyxel.pset(self.pix_x + self.size - 1, self.pix_y + self.size - 1, border_color)
            
    def destroy(self):
        self.state = SquareState.DEAD
        # render explosion
    
    def set_state(self, state):
        self.state = state
        if state == SquareState.DEAD:
            self.destroy()

    def get_state(self):
        return self.state
    
    def update(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def update_pixels(self, new_pix_x, new_pix_y):
        self.pix_x = new_pix_x
        self.pix_y = new_pix_y
        self.draw()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def print_square(self):
        print(f"Grid X: {self.x}\n Grix Y: {self.y}\nPix_x: {self.pix_x}\nPix_y: {self.pix_y}\nSize:{self.size}")