import pyxel
from square_state import SquareState

def render_centered_text(string, color, width, height):
    text_width = len(string) * pyxel.FONT_WIDTH
    title_x = (width - text_width) // 2
    pyxel.text(title_x, height // 2, string, color)
  
def not_inv(sq):
    return sq.state != SquareState.INVINCIBLE
  
# Returns [T/F,T/F,T/F,T/F] indicating whether above / below / left / right 
# squares are occupied
def calculate_adjacent_squares(x,y,grid):
    ret = [False] * 4
    if y < len(grid[x]) - 1 and (sq := grid[x][y+1]) is not None and not_inv(sq):
        ret[0] = True
    if y > 0 and (sq := grid[x][y-1]) is not None and not_inv(sq):
        ret[1] = True
    if x > 0 and (sq := grid[x-1][y]) is not None and not_inv(sq):
        ret[2] = True
    if x < len(grid) - 1 and (sq := grid[x+1][y] is not None) and not_inv(sq):
        ret[3] = True
    return ret