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

    def __init__(self, type, location, rotation_state):
        self.type = type
        #self.location = location
        x = location.x
        y = location.y
        self.squares = [Square(x, y)]*4
        self.rotation_state = 0
        match type:
            case BlockType.O:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x, y + 1)
                self.squares[3].update(x + 1, y + 1)
                self.originX = x + 0.5
                self.originY = y + 0.5
                return
            case BlockType.I:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 2, y)
                self.squares[3].update(x + 3, y)
                self.originX = x + 1.5
                self.originY = y - 0.5
                return
            case BlockType.S:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y + 1)
                self.squares[3].update(x + 2, y + 1)
                self.originX = x + 1
                self.originY = y
                return
            case BlockType.Z:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y - 1)
                self.squares[3].update(x + 2, y - 1)
                self.originX = x + 1
                self.originY = y - 1
                return
            case BlockType.L:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 2, y)
                self.squares[3].update(x + 2, y + 1)
                self.originX = x + 1
                self.originY = y
                return
            case BlockType.J:
                self.squares[1].update(x, y - 1)
                self.squares[2].update(x + 1, y - 1)
                self.squares[3].update(x + 2, y - 1)
                self.originX = x + 1
                self.originY = y - 1
                return
            case BlockType.T:
                self.squares[1].update(x + 1, y)
                self.squares[2].update(x + 1, y + 1)
                self.squares[3].update(x + 2, y)
                self.originX = x + 1
                self.originY = y
                return
            
    def rotate_helper(self, x, y, s):
        x -= self.originX
        y -= self.originY

        x_new = -y * s
        y_new = x * s

        x = x_new + self.originX
        y = y_new + self.originY

        return (x, y)

    def rotate(self, direction):
        # call update for all four squares
        (x0, y0) = (self.squares[0].getX(), self.squares[0].getY())
        (x1, y1) = (self.squares[1].getX(), self.squares[1].getY())
        (x2, y2) = (self.squares[2].getX(), self.squares[2].getY())
        (x3, y3) = (self.squares[3].getX(), self.squares[3].getY())
        match self.type:
            #case BlockType.O:
            #    return
            case BlockType.I:
                # s is sine of the angle (cosine is 0 either way)
                if (direction == Direction.LEFT):
                    s = 1
                elif (direction == Direction.RIGHT):
                    s = -1

                x0 -= self.originX
                y0 -= self.originY

                x0_new = -y0 * s
                y0_new = x0 * s
                
                x0 = x0_new + self.originX
                y0 = y0_new + self.originY

                self.squares[0].update(x0, y0)
                # if (direction == Direction.RIGHT):
                #     self.squares[1].update(x1, y1 - 1)
                #     self.squares[2].update(x1, y1 - 2)
                #     self.squares[3].update(x1, y1 - 3)
                # elif (direction == Direction.LEFT):
                #     self.squares[1].update()

        if (direction == Direction.RIGHT): self.rotation_state += 1
        elif (direction == Direction.LEFT): self.rotation_state -= 1
        self.rotation_state %= 4

        return

    def set_speed(new_speed):
        Block.blocks_speed = new_speed

    def draw():
        pass

    def destroy():
        pass
