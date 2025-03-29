import pyxel

class Paddle:
    width = 1
    height = 8
    paddle_speed = 2

    def __init__(self, w, h, player):
        self.bottomY = h - 20
        self.x = (w // 2) + 45 * (-1 if player == 1 else 1)
        self.player = player # player is 0 or 1
    
    def draw(self):
        pyxel.rect(self.x, self.bottomY, Paddle.width, Paddle.height, 3)

    def update(self):
        if pyxel.btn(pyxel.KEY_W) and self.player == 0:
            self.bottomY += Paddle.paddle_speed
        if pyxel.btn(pyxel.KEY_S) and self.player == 0:
            self.bottomY -= Paddle.paddle_speed

        if pyxel.btn(pyxel.KEY_I) and self.player == 1:
            self.bottomY += Paddle.paddle_speed
        if pyxel.btn(pyxel.KEY_K) and self.player == 1:
            self.bottomY -= Paddle.paddle_speed

        self.draw()
    
    def set_paddle_speed(new_speed):
        Paddle.paddle_speed = new_speed