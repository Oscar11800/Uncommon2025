import pyxel
from square import Square

# Game Variables (Currently dummy values)
WINNING_HEIGHT = 100

# block grid structure
# tetris blocks
# pong ball
# players (pong paddles)

class App:
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
        
        # Initialize and report assets
        pyxel.init(self.w, self.h)
        pyxel.load("./assets/block.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw_game)
    def update(self):
        if self.x == 0:
          self.grid_left[0][0] = self.make_square(0, 0)
          self.grid_left[1][0] = self.make_square(2, 0)
        self.x = (self.x + 1) % pyxel.width
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
    def make_square(self, square_idx_x, square_idx_y):
        y = self.h - self.platform_height - self.square_size * (square_idx_y + 1)
        x = self.platform_l_x + square_idx_x * self.square_size
        return Square(x, y, self.square_size, 0)
    def draw_game(self):
        pyxel.cls(6)
        # Draw static background
        left_start = self.platform_l_x
        right_start = self.platform_r_x
        platform_h = self.platform_height
        platform_w = self.platform_width
        pyxel.rect(left_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(left_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 5)
        pyxel.rect(right_start, self.h - platform_h, platform_w, platform_h, 1)
        pyxel.rect(right_start+1, self.h - platform_h+1, platform_w - 2, platform_h - 1, 5)
        # Draw all the squares
        for square in [square for row in self.grid_left for square in row]:
          if square is not None:
              square.draw()
App()

