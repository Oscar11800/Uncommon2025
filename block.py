import pyxel
from enum import Enum

import square

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

    def __init__(self, type, location, color, grid):
        self.type = type
        x = location[0]
        y = location[1]
        pix_x = grid.x_pix_offset_left + (grid.square_size * x)
        pix_y = grid.pix_height - grid.y_pix_offset_bot + (grid.square_size * y)
        self.squares = [square.Square(x, y, pix_x, pix_y, grid.square_size, color)]*4
        self.rotation_state = 0
        self.is_live = 1
        self.grid = grid
        
        match type:
            case BlockType.O:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x, y + 1)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 1, y + 1)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 0.5
                self.originY = y + 0.5
            case BlockType.I:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 2, y)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 3, y)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1.5
                self.originY = y - 0.5
            case BlockType.S:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 1, y + 1)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 2, y + 1)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1
                self.originY = y
            case BlockType.Z:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 1, y - 1)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 2, y - 1)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1
                self.originY = y - 1
            case BlockType.L:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 2, y)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 2, y + 1)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1
                self.originY = y
            case BlockType.J:
                self.squares[1].update(x, y - 1)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 1, y - 1)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 2, y - 1)
                self.squares[3].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1
                self.originY = y - 1
            case BlockType.T:
                self.squares[1].update(x + 1, y)
                self.squares[1].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[1].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[1].get_y()))
                self.squares[2].update(x + 1, y + 1)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[2].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[2].get_y()))
                self.squares[3].update(x + 2, y)
                self.squares[2].update_pixels(grid.x_pix_offset_left + (grid.square_size * self.squares[3].get_x()),
                                              grid.pix_height - grid.y_pix_offset_bot +
                                              (grid.square_size * self.squares[3].get_y()))
                self.originX = x + 1
                self.originY = y

        for i in range(len(self.squares)):
            self.grid.grid[(int)(self.squares[i-1].get_x())][(int)(self.squares[i-1].get_y())] = self.squares[i-1]
        
        self.draw()
            
    def _rotate_helper(self, x, y, s):
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
                
        self.squares[0].update(Block._rotate_helper(self, x0, y0, s))
        self.squares[1].update(Block._rotate_helper(self, x1, y1, s))
        self.squares[2].update(Block._rotate_helper(self, x2, y2, s))
        self.squares[3].update(Block._rotate_helper(self, x3, y3, s))

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

            if (self.grid[prev_x, prev_y - 1] != None):
                self.is_live = 0

    def draw(self):
        for i in len(self.squares):
            self.squares[i].draw()

    def destroy(self):
        for i in len(self.squares):
            self.squares[i].destroy()

    def slide(self, direction):
        if not self.is_live:
            return
        
        for sq in self.squares:
            if sq.getX() == 0 and direction == Direction.LEFT:
                return
            if sq.getX() == self.grid.width - 1 and direction == Direction.RIGHT:
                return
            
        for sq in self.squares:
            if direction == Direction.LEFT:
                sq.update(sq.getX() - 1, sq.getY())
            elif direction == Direction.RIGHT:
                sq.update(sq.getX() + 1, sq.getY())

    def update(self):
        if not self.is_live:
            return

        if pyxel.btn(pyxel.KEY_Q) and self.player == 0:
            self.rotate(Direction.LEFT)
        if pyxel.btn(pyxel.KEY_E) and self.player == 0:
            self.rotate(Direction.RIGHT)
        if pyxel.btn(pyxel.KEY_U) and self.player == 1:
            self.rotate(Direction.LEFT)
        if pyxel.btn(pyxel.KEY_O) and self.player == 1:
            self.rotate(Direction.RIGHT)
        
        if pyxel.btn(pyxel.KEY_A) and self.player == 0:
            self.slide(Direction.LEFT)
        if pyxel.btn(pyxel.KEY_D) and self.player == 0:
            self.slide(Direction.RIGHT)
        if pyxel.btn(pyxel.KEY_J) and self.player == 1:
            self.slide(Direction.LEFT)
        if pyxel.btn(pyxel.KEY_L) and self.player == 1:
            self.slide(Direction.RIGHT)