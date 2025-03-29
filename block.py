from enum import Enum

import square, grid

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
    is_live = 1

    def __init__(self, type, location, rotation_state, color):
        self.type = type
        x = location.x
        y = location.y
        self.squares = [square.Square(x, y, grid.Grid.SQUARE_SIZE, color)]*4
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
        if not self.is_live:
            return

        # call update for all four squares
        (x0, y0) = (self.squares[0].getX(), self.squares[0].getY())
        (x1, y1) = (self.squares[1].getX(), self.squares[1].getY())
        (x2, y2) = (self.squares[2].getX(), self.squares[2].getY())
        (x3, y3) = (self.squares[3].getX(), self.squares[3].getY())
        
        # s is sine of the angle (cosine is 0 either way)
        if (direction == Direction.LEFT):
            s = 1
        elif (direction == Direction.RIGHT):
            s = -1
                
        self.squares[0].update(Block.rotate_helper(self, x0, y0, s))
        self.squares[1].update(Block.rotate_helper(self, x1, y1, s))
        self.squares[2].update(Block.rotate_helper(self, x2, y2, s))
        self.squares[3].update(Block.rotate_helper(self, x3, y3, s))

        if (direction == Direction.RIGHT): self.rotation_state += 1
        elif (direction == Direction.LEFT): self.rotation_state -= 1
        self.rotation_state %= 4

    def set_speed(new_speed):
        Block.blocks_speed = new_speed
    
    def move_down(self):
        self.originX -= 1
        self.originY -= 1

        for i in len(self.squares):
            prev_x = self.squares[i].getX()
            prev_y = self.squares[i].getY()
            self.squares[i].update(prev_x, prev_y - 1)

            if (grid.Grid[prev_x, prev_y - 1] != None):
                self.is_live = 0

    def draw(self):
        for i in len(self.squares):
            self.squares[i].draw()

    def destroy(self):
        for i in len(self.squares):
            self.squares[i].destroy()
