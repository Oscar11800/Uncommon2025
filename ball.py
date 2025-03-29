BALL_SPEED = 1
BALL_LENGTH = 2

class Ball:
    speed = 0
    vector = (0, 0)
    position = (0, 0) # refers to top left corner of ball
    length = 0
    active_pos_list = []
    
    def __init__(self, speed, vector, position, length):
        self.speed = speed # need to initialize these
        self.vector = vector # passed in from app
        self.position = position # initialize to near center of screen
        self.length = length
        for i in range(length):
            for j in range(length):
                self.active_pos_list.append((self.position[0] + (i - 1), self.position[1] + (j - 1)))

    def set_speed(self, speed):
        self.speed = speed

    def set_vector(self, vector):
        self.vector = vector
    
    def set_position(self, position):
        self.position = position

    def set_length(self, length):
        self.length = length

    def get_speed(self):
        return self.speed
    
    def get_vector(self):
        return self.vector
    
    def get_position(self):
        return self.position

    def get_length(self):
        return self.length
    

