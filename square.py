import pyxel
from enum import Enum
from utils import calculate_adjacent_squares
# representation of NxN pixel square in terms of grid size  (not pixels)
# Note: x,y are in terms of coordinates on the play-area grid 

class SquareState(Enum):
    SET = 0
    LIVE = 1
    DEAD = 2
    INVINCIBLE = 3
  
class Colors(Enum):
    TEAM_1_INNER = 5
    TEAM_1_OUTER = 4
    TEAM_2_INNER = 7
    TEAM_2_OUTER = 6

# A square is always a unit size in terms of the grid
class Square:
    def __init__(self, x, y, u, v, size, team):
        # pixel coordinates
        self.x = x
        self.y = y
        # grid coordinates
        self.u = u
        self.v = v
        # pixel size
        self.width = size
        self.length = size
        self.size = size # size is in terms of pixels
        self.state = SquareState.LIVE
        self.team = team
        
    def draw(self, grid):
        color = Colors.TEAM_1_INNER.value if self.team == 1 else Colors.TEAM_2_INNER.value
        pyxel.rect(self.x, self.y, self.width, self.length, color)
        # Calculate borders
        adjacent_squares = calculate_adjacent_squares(self.u, self.v, grid)
        border_color = Colors.TEAM_1_OUTER.value if self.team == 1 else Colors.TEAM_2_OUTER.value
        if not adjacent_squares[0]:
            pyxel.rect(self.x, self.y, self.width, 1, border_color)
        if not adjacent_squares[1]:
            pyxel.rect(self.x, self.y + self.length - 1, self.width, 1, border_color)
        if not adjacent_squares[2]:
            pyxel.rect(self.x, self.y, 1, self.length, border_color)
        if not adjacent_squares[3]:
            pyxel.rect(self.x + self.width - 1, self.y, 1, self.length, border_color)
    
    def destroy(self):
        self.state = SquareState.DEAD
        # render explosion
    
    def set_state(self, state):
        self.state = state
        if state == SquareState.DEAD:
            self.destroy()
        
    def update(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.draw()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y