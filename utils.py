import pyxel

def render_centered_text(string, color, width, height):
    text_width = len(string) * pyxel.FONT_WIDTH
    title_x = (width - text_width) // 2
    pyxel.text(title_x, height // 2, string, color)