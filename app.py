import pyxel
from square import Square
from square_state import SquareState
from ball import Ball
from paddle import Paddle
from utils import render_centered_text, horizontal_or_vertical_collision
from grid import Grid

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

    def __init__(self):
        # Config game window
        self.w = 192
        self.h = 108
        
        # Set pixel size of square
        self.square_size = self.w // 25
        print("Square size:", self.square_size)
        
        # Set grid size in squares
        self.grid_width_in_squares = 6
        self.grid_height_in_squares = 20
        
        # Set platform dimensions
        self.platform_height_pix = 2
        self.platform_width = self.square_size * self.grid_width_in_squares
        self.platform_height_pix = self.platform_height_pix
        self.platform_l_x = self.w * 0.025
        self.platform_r_x = self.w * 0.975 - self.platform_width
        
        # Instantiate grids (TODO: Double check params, may be wrong)
        self.grid_left = Grid(self.square_size, self.grid_height_in_squares, self.grid_width_in_squares, self.platform_l_x, 0, self.platform_height_pix)
        
        self.grid_right = Grid(self.square_size, self.grid_height_in_squares, self.grid_width_in_squares, self.platform_r_x, 0, self.platform_height_pix)

        # Instantiate paddles
        self.paddles = [Paddle(self.w,self.h, 0), Paddle(self.w, self.h, 1)]
        
        # Instantiate ball
        ball_init_x = (self.w // 2) - (BALL_LENGTH // 2)
        ball_init_y = (self.h // 2) - (BALL_LENGTH // 2)
        ball_init_pos = (ball_init_x, ball_init_y)
        self.game_ball = Ball(1, (0, 0), ball_init_pos, BALL_LENGTH)

        # Track index of each player in the list of block shapes
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
    
    def start_game(self):
        pass
    # Check/Fix Functions
    def check_collisions(self):
        active_grid = self.grid_left if self.game_ball.position[0] < self.w // 2 else self.grid_right
        min_x, max_x = self.game_ball.position[0], self.game_ball.position[0] + self.game_ball.length
        min_y, max_y = self.game_ball.position[1], self.game_ball.position[1] + self.game_ball.length
        ball_cords = set([(i,j) for i in range(min_x, max_x) for j in range(min_y, max_y)])
        for square in [square for row in active_grid for square in row]:
            if square is not None:
                sqr_x1, sqr_y1 = square.x, square.y
                sqr_x2, sqr_y2 = square.x + square.size, square.y + square.size
                square_cords = set([(i,j) for i in range(sqr_x1, sqr_x2) for j in range(sqr_y1, sqr_y2)])
                if (overlap := ball_cords.intersection(square_cords)):
                  intersect = list(overlap)[0]
                  vertical_collision = horizontal_or_vertical_collision(
                    self.game_ball.position[0], self.game_ball.position[1], 
                    square.x, square.y, self.game_ball.length
                  )
                  # if vertical, then invert the horizontal component of velocity
                  self.game_ball.vector[0] *= -1
                  # if horizontal, invert the vertical component
                  self.game_ball.vector[0] *= -1
                  # also remove this square
                  square.state = SquareState.DEAD
                  
                  
    def check_setblocks(self): # TO-DO: convert live blocks 
       pass
    def player_wins(self, winning_player): # TO-DO: DUMMY IMPLEMENTATION
       pyxel.text(0, 0, "PLAYER {winning_player} WINS!")
       pyxel.quit()
    def check_win_con(self):
        if self.grid_left.check_win(WINNING_HEIGHT):
           self.player_wins(1)
        elif self.grid_right.check_win(WINNING_HEIGHT):
           self.player_wins(2)
    def fix_missing_live_blocks(self): # checks if either grid is missing a live block and respawns one if so
        if not self.grid_left.has_live():
          self.grid_left.spawn_block(self.player1_block_index)
        if not self.grid_right.has_live():
          self.grid_right.spawn_block(self.player2_block_index)

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
        self.x = self.x + 1

        self.paddles[0].update()
        self.paddles[1].update()
        
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
        y = self.h - self.platform_height_pix - self.square_size * (square_idx_y + 1)
        x = left_x + square_idx_x * self.square_size
        square = Square(x, y, square_idx_x, square_idx_y, self.square_size, team)
        if team == 1:
          self.grid_left.grid[square_idx_y][square_idx_x] = square
        else:
          self.grid_right.grid[square_idx_y][square_idx_x] = square
        return square
      
    def draw_game(self):
        pyxel.cls(0)
        # Draw background name
        render_centered_text("TETRISN'T", 8, self.w, self.h)
        # Calculate platform location
        left_start = self.platform_l_x
        right_start = self.platform_r_x
        platform_h = self.platform_height_pix
        platform_w = self.platform_width
        
        # Render platforms
        pyxel.rect(left_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(left_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 2)
        pyxel.rect(right_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(right_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 2)
        
        # Remove the top border of the bottom platform if there are other invincible rows
        if self.grid_left.grid[0][0] is not None and self.grid_left.grid[0][0].state == SquareState.INVINCIBLE:
            pyxel.rect(left_start + 1, self.h - platform_h, platform_w - 2, 1, 2)
        if self.grid_right.grid[0][0] is not None and self.grid_right.grid[0][0].state == SquareState.INVINCIBLE:
            pyxel.rect(right_start + 1, self.h - platform_h, platform_w - 2, 1, 2)
            
        # Draw all the squares
        for square in [square for row in self.grid_left.grid for square in row]:
          if square is not None:
              square.draw(self.grid_left.grid)
        for square in [square for row in self.grid_right.grid for square in row]:
          if square is not None:
              square.draw(self.grid_right.grid)
        for paddle in self.paddles:
          paddle.draw()
        self.game_ball.draw()
App()

