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

class Block:
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

    def update():
        # call update for all four blocks
        pass

    def draw():
        pass

    def destroy():
        pass
