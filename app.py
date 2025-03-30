import pyxel
from square import Square
from square_state import SquareState
from ball import Ball
from paddle import Paddle
from utils import render_centered_text, horizontal_or_vertical_collision, bfs
from grid import Grid
from playsound import playsound
import threading
import os
import time

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

    def music(sound):
        while True:
          playsound(sound)

    def __init__(self):
        # avoid delays on first sound play
        #threading.Thread(target=playsound, args=('assets\\silent_quarter-second.wav',), daemon=True).start()

        self.music = threading.Thread(target=App.music, args=(os.path.dirname(__file__) + '\\assets\\background_music_first_half.mp3',), daemon=True).start()

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
        self.game_ball = Ball(1, (10, 10), ball_init_pos, BALL_LENGTH)

        # Track index of each player in the list of block shapes
        self.player1_block_index = 0
        self.player2_block_index = 0

        # Instantiate live blocks
        self.left_live_block = None
        self.right_live_block = None

        # Initialize and report assets
        pyxel.init(self.w, self.h)
        pyxel.load("./assets/block.pyxres")
        pyxel.colors.from_list([
          0x121019, 0x3D3D3D, 0x525252, 
          0xF2F2F2, 0x1F4283, 0x226CE0, 
          0x853D3B, 0xEF6351, 0x2D283E
        ])
        self.curr_frame = 0
        
        self.game_running = False
        
        pyxel.run(self.update, self.draw_game)
    
    # Initiatiate game timer, ball velocity, and start dropping blocks
    def start_game(self):
        self.game_running = False
        self.start_time = time.time()
        
    
    # Check/Fix Functions
    def check_collisions(self):
        active_grid = self.grid_left if self.game_ball.position[0] < self.w // 2 else self.grid_right
        min_x, max_x = self.game_ball.position[0], self.game_ball.position[0] + self.game_ball.length
        min_y, max_y = self.game_ball.position[1], self.game_ball.position[1] + self.game_ball.length
        ball_cords = set([(i,j) for i in range(min_x, max_x) for j in range(min_y, max_y)])
        for square in [square for row in active_grid.grid for square in row]:
            if square is not None:
                sqr_x1, sqr_y1 = int(square.x), int(square.y)
                sqr_x2, sqr_y2 = int(square.x + square.size), int(square.y + square.size)
                square_cords = set([(i,j) for i in range(sqr_x1, sqr_x2) for j in range(sqr_y1, sqr_y2)])
                if (overlap := ball_cords.intersection(square_cords)):
                  intersect = list(overlap)[0]
                  vertical_collision = horizontal_or_vertical_collision(
                    self.game_ball.position[0], self.game_ball.position[1], 
                    square.x, square.y, self.game_ball.length
                  )
                  # if vertical, then invert the horizontal component of velocity
                  self.game_ball.vector[1] *= -1
                  # if horizontal, invert the vertical component
                  self.game_ball.vector[0] *= -1
                  # also remove this square
                  if square.state == SquareState.LIVE:
                    print("dead square")
                    square.state = SquareState.DEAD
                    threading.Thread(target=playsound, args=('assets\\non_invincible_block_hit.wav',), daemon=True).start()
                  elif square.state == SquareState.INVINCIBLE:
                    threading.Thread(target=playsound, args=('assets\\invincible_block_hit.wav',), daemon=True).start()
        for paddle in self.paddles: # collisions are all horizontal
          if self.game_ball.position[0] >= paddle.x - 1 and self.game_ball.position[0] <= paddle.x + 1 and self.game_ball.position[1] >= paddle.bottomY and self.game_ball.position[1] <= paddle.bottomY + Paddle.height:
            self.game_ball.vector[0] *= -1
            threading.Thread(target=playsound, args=('assets\\paddle_hit.wav',), daemon=True).start()
          # if self.game_ball.position[0] == paddle.x - 1 and self.game_ball.position[1] >= paddle.bottomY and self.game_ball.position[1] <= paddle.bottomY + Paddle.height:
          #   self.game_ball.vector[0] *= -1
          #   threading.Thread(target=playsound, args=('assets\\paddle_hit.wav',), daemon=True).start()
        for i in range(len(active_grid.grid)):
            for j in range(len(active_grid.grid[i])):
                square = self.grid_left.grid[i][j]
                if square is not None and square.state == SquareState.DEAD:
                    self.grid_left.destroy_square(i, j)
        if self.game_ball.position[1] <= 0:
            self.game_ball.vector[1] *= -1
        if self.game_ball.position[1] >= self.h - self.game_ball.length:
            self.game_ball.vector[1] *= -1
        if self.game_ball.position[0] <= 0 or self.game_ball.position[0] >= self.w - self.game_ball.length: 
            self.game_ball.vector[0] *= -1
                  
                  
    def check_setblocks(self): # TO-DO: convert live blocks 
       blocks_to_set = []
       visited = set()
       rows, cols = len(self.grid_left), len(self.grid_right[0])
       for r in range(rows):
           for c in range(cols):
               if (self.grid_left[r][c].get_state() == SquareState.LIVE and  (r,c) not in visited):
                   blocks_to_set.append(self.grid_left[r][c])
                   bfs(r,c, visited, rows, cols, self.grid_left)
        
               
   
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
        self.player1_block_index += 1
      if not self.grid_right.has_live():
        self.grid_right.spawn_block(self.player2_block_index)
        self.player2_block_index += 1

    def update(self):
        if(self.curr_frame == 0 and pyxel.btn(pyxel.KEY_Z)):
            self.game_running = True
            print("YES")
            self.start_game()
                
        
        if self.curr_frame == 0:
        #   self.make_square(0, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(1, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(2, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(3, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(4, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(5, 0, 1).set_state(SquareState.INVINCIBLE)
        #   self.make_square(0, 5, 1)
        #   self.make_square(0, 7, 1)
        #   self.make_square(0, 4, 1)
        #   self.make_square(0, 1, 1)
        #   self.make_square(2, 0, 2)
            self.left_live_block = self.grid_left.spawn_block(self.player1_block_index)
            # I was here.
            self.right_live_block = self.grid_right.spawn_block(self.player2_block_index)
            self.game_ball.set_vector([game_ball.speed, 0])
          
        if(self.game_running):
            self.curr_frame = self.curr_frame + 1

            self.paddles[0].update()
            self.paddles[1].update()

            # check for collisions
            self.check_collisions()
            # update ball
            self.game_ball.set_position((self.game_ball.position[0] + self.game_ball.vector[0], self.game_ball.position[1] + self.game_ball.vector[1]))
        self.fix_missing_live_blocks()

        if self.player1_block_index >= 1 or self.player2_block_index >= 1:
          self.music.join()
          self.music = threading.Thread(target=App.music, args=(os.path.dirname(__file__) + '\\assets\\background_music_second_half.mp3',), daemon=True).start()
        
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.curr_frame, 0, 8, 8, 9)
    
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
        render_centered_text("TETRIS", 4, self.w -14, self.h)
        render_centered_text("N'T", 6, self.w + 22, self.h)
        
        if self.game_running:
            pyxel.text(22 *pyxel.FONT_WIDTH, (self.h - 100) //2, str(round(time.time() - self.start_time, 2)), 1)

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

        # Render Win-Line
        pyxel.rect(left_start, self.h - WINNING_HEIGHT, platform_w, 2, 2)
        pyxel.rect(right_start, self.h - WINNING_HEIGHT, platform_w, 2, 2)
        
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

