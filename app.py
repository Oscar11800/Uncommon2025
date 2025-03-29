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
        pyxel.run(self.update, self.draw)
    def update(self):
        self.x = (self.x + 1) % pyxel.width
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 2, 2, 9)

App()