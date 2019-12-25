import pygame
from block import MyBlock, TargetBlock
from global_info import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Swap ME")

screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
FPS = 2

def create_grid(locked_positions={}):
    cols = int(play_width / grid_size)
    rows = int(play_height / grid_size)
    
    grid = [[(128, 128, 128) for x in range(cols)] for x in range(rows)]
 
    for i in range(len(grid)):# rows
        for j in range(len(grid[i])):# cols
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def draw_grid(screen, grid):
    for i in range(len(grid)):# rows
        for j in range(len(grid[i])):# cols
            pygame.draw.rect(screen, grid[i][j], (top_left_x + j* grid_size, top_left_y + i * grid_size, grid_size, grid_size), 1)
            
    pygame.draw.rect(screen, RED, [top_left_x, top_left_y, play_width, play_height], 3)

def draw_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont('comicsansms', 30, True)
    label = font.render('SwapME', 1, WHITE)    
    screen.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y / 2 - (label.get_height() / 2)))

    draw_grid(screen, grid)
    
    myBlock.draw(screen)
    targetBlock.draw(screen)
    
    pygame.display.update()

# mainloop
global grid

run = True
level = 1
locked_positions = {}  # (x,y):(255,0,0)
grid = create_grid(locked_positions)
myBlock = MyBlock(top_left_x, top_left_y, block_width, block_height, level+2)
targetBlock = TargetBlock(width - target_offset_width, 150, block_width, block_height, level+2)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_screen()

pygame.quit()