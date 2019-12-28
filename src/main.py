import pygame
from block import MyBlock, TargetBlock
from global_info import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Swap ME")

screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
FPS = 5

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
    
    currentBlock.draw(screen)
    targetBlock.draw(screen)
    
    pygame.display.update()

def valid_move(block):
    min_x = top_left_x
    max_x = top_left_x + play_width

    is_valid_left = False
    is_valid_right = False

    if block.x > min_x:
        is_valid_left = True
        
    if block.x + block.width < max_x:
        is_valid_right = True

    return [is_valid_left, is_valid_right]

# mainloop
# global grid

run = True
level = 1
block_counts = level + 2

locked_positions = {}  # (x,y):(255,0,0)
grid = create_grid(locked_positions)
currentBlock = MyBlock(top_left_x, top_left_y, block_width, block_height, block_counts)
targetBlock = TargetBlock(width - target_offset_width, 150, block_width, block_height, block_counts)
newBlock = False

while run:
    clock.tick(FPS)

    [LeftMove, RightMove] = valid_move(currentBlock)
    # check if current block is arrived at bottom
    if currentBlock.y + currentBlock.height*block_counts >= top_left_y+play_height:
        pygame.time.wait(500)
        newBlock = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if LeftMove:
                    currentBlock.x -= grid_size
            elif event.key == pygame.K_RIGHT:
                if RightMove:
                    currentBlock.x += grid_size
            elif event.key == pygame.K_UP:
                if currentBlock.focus_block > 0:
                    currentBlock.focus_block -= 1
            elif event.key == pygame.K_DOWN:
                if currentBlock.focus_block < block_counts - 1:
                    currentBlock.focus_block += 1
            elif event.key == pygame.K_SPACE:
                # SWAP. 현재 선택 블록과 바로 윗 블록 바꾸기
                currentBlock.colors[currentBlock.focus_block], currentBlock.colors[currentBlock.focus_block - 1] \
                    = currentBlock.colors[currentBlock.focus_block - 1], currentBlock.colors[currentBlock.focus_block]
            elif event.key == pygame.K_RETURN:# ENTER KEY
                currentBlock.y = top_left_y + play_height - currentBlock.height * block_counts

    if newBlock:
        currentBlock = MyBlock(top_left_x, top_left_y, block_width, block_height, block_counts)
        
        newBlock = False

    draw_screen()

pygame.quit()