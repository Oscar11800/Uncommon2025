import pyxel

class Paddle:
    width = 1
    height = 8
    paddle_speed = 2

    def __init__(self, bottomY, player):
        self.bottomY = bottomY
        self.player = player # player is 0 or 1
        self.x = 30 + (40 * player)
    
    def draw(self):
        pyxel.rect(self.x, self.bottomY, Paddle.width, Paddle.height, 0)

    def update(self):
        if pyxel.btn(pyxel.KEY_W) and self.player == 0:
            self.bottomY += Paddle.paddle_speed
        if pyxel.btn(pyxel.KEY_S) and self.player == 0:
            self.bottomY -= Paddle.paddle_speed

        if pyxel.btn(pyxel.KEY_UP) and self.player == 1:
            self.bottomY += Paddle.paddle_speed
        if pyxel.btn(pyxel.KEY_DOWN) and self.player == 1:
            self.bottomY -= Paddle.paddle_speed

        self.draw()
    
    def set_paddle_speed(new_speed):
        Paddle.paddle_speed = new_speed