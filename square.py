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
    def __init__(self, x, y, u, v, size, player):
        # pixel coordinates
        self.x = x
        self.y = y
        # grid coordinates
        self.u = u
        self.v = v
        # pixel size
        self.size = size # size is in terms of pixels
        self.state = SquareState.LIVE
        self.player = player
        
    def draw_invincible(self,grid):
        COLOR_INNER = 2
        COLOR_OUTER = 1
        pyxel.rect(self.x, self.y, self.size, self.size, COLOR_INNER)
        if self.u == 0:
            pyxel.rect(self.x, self.y, 1, self.size, COLOR_OUTER)
        if self.u == len(grid[0]) - 1:
            pyxel.rect(self.x + self.size - 1, self.y, 1, self.size, COLOR_OUTER)
        if self.v == len(grid) - 1:
            pyxel.rect(self.x, self.y, 1, self.size, COLOR_OUTER)
        else:
            square_above = grid[self.u + 1][self.v]
            if square_above is None or square_above.state != SquareState.INVINCIBLE:
                pyxel.rect(self.x, self.y, self.size, 1, COLOR_OUTER)
            else:
              print(square_above.state)
        
    def draw(self, grid):
        if self.state == SquareState.INVINCIBLE:
            return self.draw_invincible(grid)
        color = Colors.PLAYER_1_INNER.value if self.player == 1 else Colors.PLAYER_2_INNER.value
        pyxel.rect(self.x, self.y, self.size, self.size, color)
        # Calculate borders
        adjacent_squares = calculate_adjacent_squares(self.u, self.v, grid)
        border_color = Colors.PLAYER_1_OUTER.value if self.player == 1 else Colors.PLAYER_2_OUTER.value
        # Borders
        if not adjacent_squares[0]:
            pyxel.rect(self.x, self.y, self.size, 1, border_color)
        if not adjacent_squares[1]:
            pyxel.rect(self.x, self.y + self.size - 1, self.size, 1, border_color)
        if not adjacent_squares[2]:
            pyxel.rect(self.x, self.y, 1, self.size, border_color)
        if not adjacent_squares[3]:
            pyxel.rect(self.x + self.size - 1, self.y, 1, self.size, border_color)
        # Corners
        if adjacent_squares[0] and adjacent_squares[2]:
            pyxel.pset(self.x, self.y, border_color)
        if adjacent_squares[0] and adjacent_squares[3]:
            pyxel.pset(self.x + self.size - 1, self.y, border_color)
        if adjacent_squares[1] and adjacent_squares[2]:
            pyxel.pset(self.x, self.y + self.size - 1, border_color)
        if adjacent_squares[1] and adjacent_squares[3]:
            pyxel.pset(self.x + self.size - 1, self.y + self.size - 1, border_color)
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
        self.draw()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y