from pathlib import Path

from PIL import ImageFont


# Color scheme
class Colors:
    background = (41, 45, 52, 255)
    primary = (144, 176, 97, 255)
    secondary = (190, 138, 89, 255)
    highlight = (157, 163, 157, 255)
    text_default = (240, 244, 250, 255)
    divider = text_default


# standard 1920x1080 at 1 fps
FPS = 1
FRAME_WIDTH = 1920
FRAME_HEIGHT = 1080

# line exec section of canvas
LE_XSTART = 7 / 10 * FRAME_WIDTH
LE_YSTART = 0.07 * FRAME_HEIGHT

# variable section of canvas
VAR_XSTART = 7 / 10 * FRAME_WIDTH
VAR_YSTART = LE_YSTART

# text properties
LINE_PADDING = 10
FONT_SIZE = 20
FONT_DIR = Path(__file__).parent / "fonts"
FONT = ImageFont.truetype(str(FONT_DIR / "consolas.ttf"), FONT_SIZE)
