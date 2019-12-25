# Define the colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (50, 0, 50)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)

# Screen Info
screen_size = width, height = 600, 600
play_size = play_width, play_height = 300, 480
target_offset_width = 100
top_left_x = (width - target_offset_width - play_width) // 2
top_left_y = (height - play_height) // 2
block_size = block_width, block_height = 60, 30
grid_size = 30