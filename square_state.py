from enum import Enum

class SquareState(Enum):
    SET = 0
    LIVE = 1
    DEAD = 2
    INVINCIBLE = 3