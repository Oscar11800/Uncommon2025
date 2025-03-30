from playsound import playsound
from multiprocessing import Process

class Music(Process):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound
    def run(self):
        while True:
            playsound(self.sound)