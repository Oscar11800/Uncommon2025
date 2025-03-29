import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256)
        self.x = 0
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw