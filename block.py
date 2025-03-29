import pyxel

from enum import Enum

class BlockType(Enum):
    O = 1
    I = 2
    S = 3
    Z = 4
    L = 5
    J = 6
    T = 7

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class Block:
    blocks_speed = 1 # speed of blocks falling

    def __init__(self, type, location):
        self.type = type
        #self.location = location
        x = location.x
        y = location.y
        self.squares = [Square(x, y)]*4
        match type:
            case BlockType.O:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x, y + 1)
                self.squares[3].update(x + 1, y + 1)
                return
            case BlockType.I:
                self.squares[1].update(x, y + 1)
                self.squares[2].update(x, y + 2)
                self.squares[3].update(x, y + 3)
                return
            case BlockType.S:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y + 1)
                self.squares[3].update(x + 2, y + 1)
                return
            case BlockType.Z:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y - 1)
                self.squares[3].update(x + 2, y - 1)
                return
            case BlockType.L:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x, y + 1)
                self.squares[3].update(x, y + 2)
                return
            case BlockType.J:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y + 1)
                self.squares[3].update(x + 1, y + 2)
                return
            case BlockType.T:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y - 1)
                self.squares[3].update(x + 2, y)
                return

    def rotate(self, direction):
        # call update for all four squares
        (x1, y1) = (self.squares[1].getX(), self.squares[1].getY())
        (x2, y2) = (self.squares[2].getX(), self.squares[2].getY())
        (x3, y3) = (self.squares[3].getX(), self.squares[3].getY())
        (x4, y4) = (self.squares[4].getX(), self.squares[4].getY())
        match self.type:
            case BlockType.O:
                return
            case BlockType.I:
                is_horizontal = (x2 > x1)
                if (is_horizontal):
                    if (direction == Direction.RIGHT):
                        self.squares[1].update(x1, y1 - 1)
                        self.squares[2].update(x1, y1 - 2)
                        self.squares[3].update(x1, y1 - 3)
                    elif (direction == Direction.LEFT):
                        self.squares[1].update()
        pass

    def set_speed(new_speed):
        Block.blocks_speed = new_speed

    def draw():
        pass

    def destroy():
        pass
