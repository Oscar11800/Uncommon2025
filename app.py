import pyxel

# Game Variables (Currently dummy values)
BALL_SPEED = 1
BALL_LENGTH = 2
WINNING_HEIGHT = 100



# block grid structure
# tetris blocks
# pong ball
# players (pong paddles)

class App:
    def __init__(self):
        pyxel.init(192, 108)
        self.x = 0
        pyxel.run(self.update, self.draw_game)
    def update(self):
        self.x = (self.x + 1) % pyxel.width
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
    def draw_game(self):
        pyxel.cls(6)
        # Draw static background
        w = pyxel.width
        h = pyxel.height
        square_size = w // 30
        platform_width_in_squares = 6
        platform_height = 3
        platform_width = square_size * platform_width_in_squares
        play_left_start = w * 0.05
        play_right_start = w * 0.95 - platform_width
        pyxel.rect(play_left_start, h - platform_height, platform_width, platform_height, 1)
        pyxel.rect(play_left_start+1, h - platform_height+1, platform_width - 2, platform_height - 1, 5)
        pyxel.rect(play_right_start, h - platform_height, platform_width, platform_height, 1)
        pyxel.rect(play_right_start+1, h - platform_height+1, platform_width - 2, platform_height - 1, 5)
        # Draw all the squares
App()

