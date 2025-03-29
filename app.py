import pyxel
import random
from square import Square
from square_state import SquareState
from ball import Ball
from utils import render_centered_text

# Game Settings (Currently dummy values)
WINNING_HEIGHT = 100
BALL_LENGTH = 2

# block grid structure
# tetris blocks
# pong ball
# players (pong paddles)

class App:
    # Game Object List
    # w = width, h = height, square_size, grid_width_in_squares, platform_height, platform_width,
    # platform_l_x, platform_r_x, grid_left, game_ball

    block_list = random.choices(range(1, 8), k=500) # generate 500 random block types

    def __init__(self):
        # Config
        self.w = 192
        self.h = 108
        self.square_size = self.w // 25
        print("Square size:", self.square_size)
        self.grid_width_in_squares = 6
        self.grid_height_in_squares = 20
        self.platform_height = 2
        # Prepare for rendering
        self.platform_width = self.square_size * self.grid_width_in_squares
        self.platform_height = self.platform_height
        self.platform_l_x = self.w * 0.025
        self.platform_r_x = self.w * 0.975 - self.platform_width
        # Maintain state
        self.grid_left = [[None] * self.grid_width_in_squares for _ in range(self.grid_height_in_squares)]
        self.grid_right = [[None] * self.grid_width_in_squares for _ in range(self.grid_height_in_squares)]
        
        ball_init_x = (self.w // 2) - (BALL_LENGTH // 2)
        ball_init_y = (self.h // 2) - (BALL_LENGTH // 2)
        ball_init_pos = (ball_init_x, ball_init_y)
        self.game_ball = Ball(1, (0, 0), ball_init_pos, BALL_LENGTH)

        self.player1_block_index = 0
        self.player2_block_index = 0

        # Initialize and report assets
        pyxel.init(self.w, self.h)
        pyxel.load("./assets/block.pyxres")
        pyxel.colors.from_list([
          0x121019, 0x3D3D3D, 0x525252, 
          0xF2F2F2, 0x1F4283, 0x226CE0, 
          0x853D3B, 0xEF6351, 0x2D283E
        ])
        self.x = 0
        pyxel.run(self.update, self.draw_game)
    
    # Check Functions
    def check_collisions(self):
       pass
    def check_setblocks(self):
       pass
    def win_con(self):
       pass
    def check_missing_live_blocks(self):
       pass

    # Update/Rendering
    def update(self):
        if self.x == 0:
          self.make_square(0, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(1, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(2, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(3, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(4, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(5, 0, 1).set_state(SquareState.INVINCIBLE)
          self.make_square(0, 1, 1)
          self.make_square(2, 0, 2)
        self.x = (self.x + 1) % pyxel.width
        
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
    
    # Team should be 1 if left, 2 if right
    # Number placement is such that 
    # ...
    # (1,1), (2,1)...
    # (0,0), (1,0)...
    # =============== (floor)
    def make_square(self, square_idx_x, square_idx_y, team):
        left_x = self.platform_l_x if team == 1 else self.platform_r_x
        y = self.h - self.platform_height - self.square_size * (square_idx_y + 1)
        x = left_x + square_idx_x * self.square_size
        square = Square(x, y, square_idx_x, square_idx_y, self.square_size, team)
        if team == 1:
          self.grid_left[square_idx_y][square_idx_x] = square
        else:
          self.grid_right[square_idx_y][square_idx_x] = square
        return square
      
    def draw_game(self):
        pyxel.cls(0)
        # Draw background name
        render_centered_text("TETRISN'T", 8, self.w, self.h)
        # Calculate platform location
        left_start = self.platform_l_x
        right_start = self.platform_r_x
        platform_h = self.platform_height
        platform_w = self.platform_width
        # Render platforms
        pyxel.rect(left_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(left_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 2)
        pyxel.rect(right_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(right_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 2)
        # Remove the top border of the bottom platform if there are other invincible rows
        if self.grid_left[0][0] is not None and self.grid_left[0][0].state == SquareState.INVINCIBLE:
            pyxel.rect(left_start + 1, self.h - platform_h, platform_w - 2, 1, 2)
        if self.grid_right[0][0] is not None and self.grid_right[0][0].state == SquareState.INVINCIBLE:
            pyxel.rect(right_start + 1, self.h - platform_h, platform_w - 2, 1, 2)
        # Draw all the squares
        for square in [square for row in self.grid_left for square in row]:
          if square is not None:
              square.draw(self.grid_left)
        for square in [square for row in self.grid_right for square in row]:
          if square is not None:
              square.draw(self.grid_right)

App()

