class Ball:
    speed = 0
    vector = (0, 0)
    position = (0, 0)
    
    def __init__(self, speed, vector, position):
        self.speed = speed # need to initialize these
        self.vector = vector # passed in from app
        self.position = position # initialize to center of screen

    def set_speed(self, speed):
        self.speed = speed

    def set_vector(self, vector):
        self.vector = vector
    
    def set_position(self, position):
        self.position = position

    def get_speed(self):
        return self.speed
    
    def get_vector(self):
        return self.vector
    
    def get_position(self):
        return self.position
    

