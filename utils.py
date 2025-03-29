import pyxel

def render_centered_text(string, color, width, height):
    text_width = len(string) * pyxel.FONT_WIDTH
    title_x = (width - text_width) // 2
    pyxel.text(title_x, height // 2, string, color)
  
# Returns [T/F,T/F,T/F,T/F] indicating whether above / below / left / right 
# squares are occupied
def calculate_adjacent_squares(x,y,grid):
    ret = [False] * 4
    if y < len(grid[x]) - 1 and grid[x][y+1] is not None:
        ret[0] = True
    if y > 0 and grid[x][y-1] is not None:
        ret[1] = True
    if x > 0 and grid[x-1][y] is not None:
        ret[2] = True
    if x < len(grid) - 1 and grid[x+1][y] is not None:
        ret[3] = True
    return ret