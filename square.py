import pyxel
from enum import Enum
# representation of NxN pixel square in terms of grid size  (not pixels)
# Note: x,y are in terms of coordinates on the play-area grid 

class SquareState(Enum):
    SET = 0
    LIVE = 1
    DEAD = 2

class Square:
    def _init_(self, x, y, size):
        self.x = x
        self.y = y
        self.width = 1
        self.length = 1
        self.size = size 
        self.state = SquareState.LIVE
        
    def draw(self):
        pyxel.rect(self.x, self.y)
    
    def destroy(self):
        self.state = SquareState.DEAD
        # render explosion
    
    def set_state(self, state):
        self.state = state
        
    def update(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.draw()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y