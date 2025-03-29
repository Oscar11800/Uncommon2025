import pyxel
from enum import Enum
# representation of NxN pixel square in terms of grid size  (not pixels)
# Note: x,y are in terms of coordinates on the play-area grid 

class SquareState(Enum):
    SET = 0
    LIVE = 1
    DEAD = 2
    INVINCIBLE = 3

# A square is always a unit size in terms of the grid
class Square:
    def __init__(self, x, y, size, team):
        self.x = x
        self.y = y
        self.width = size
        self.length = size
        self.size = size # size is in terms of pixels
        self.state = SquareState.LIVE
        self.team = team
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 7, 7, 7, 7)
        #pyxel.rect(self.x, self.y, self.width, self.length, self.color)
    
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