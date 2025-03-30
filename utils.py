from collections import deque
import pyxel
from square_state import SquareState

def bfs(r, c, visited, rows, cols, grid):
     q = deque()
     visited.add((r, c))
     q.append((r, c))

     while q:
         row, col = q.popleft()
         directions = [[1,0],[-1,0],[0,1],[0,-1]]

         for dr, dc in directions:
             r, c = row + dr, col + dc
             if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                 q.append((r, c))
                 visited.add((r, c))

def render_centered_text(string, color, width, height):
    text_width = len(string) * pyxel.FONT_WIDTH
    title_x = (width - text_width) // 2
    pyxel.text(title_x, height // 2, string, color)
  
def not_inv(sq):
    return sq.state != SquareState.INVINCIBLE
  
# Returns [T/F,T/F,T/F,T/F] indicating whether above / below / left / right 
# squares are occupied
def calculate_adjacent_squares(y, x, grid):
    ret = [False] * 4
    if y < grid.height - 1 and (sq := grid.get_grid()[x][y+1]) is not None and not_inv(sq):
        ret[2] = True
    if y > 0 and (sq := grid.get_grid()[x][y-1]) is not None and not_inv(sq):
        ret[3] = True
    if x > 0 and (sq := grid.get_grid()[x-1][y]) is not None and not_inv(sq):
        ret[1] = True
    if x < grid.width - 1 and (sq := grid.get_grid()[x+1][y]) is not None and not_inv(sq):
        ret[0] = True
    return ret

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  
# Return TRUE if vertical, FALSE is horizontal, 
def horizontal_or_vertical_collision(x,y,u,v,size):
    distances = [
      (distance(u,v,x,y), 0),
      (distance(u+size,v,x,y), 1),
      (distance(u,v,x,y+size), 2),
      (distance(u+size,v,x,y+size), 3),
    ]
    distances.sort()
    return distances[0][1] % 2 == distances[1][1] % 2