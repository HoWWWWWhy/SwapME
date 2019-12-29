import pygame
import random
from global_info import *

BLOCK_COLORS = [BLUE, GREEN, RED, YELLOW, PURPLE, ORANGE, CYAN]

class MyBlock(object):

    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.colors = []
        self.y_update_counter = 0
        self.focus_block = number-1#focus on bottom block

        self.color_set()

    def color_set(self):#중복되지 않도록 블록 색깔 뽑기
        for i in range(self.number):
            random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            while random_color in self.colors:
                random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            self.colors.append(random_color) 
            
    def draw(self, screen):
        for i in range(self.number):
            pygame.draw.rect(screen, self.colors[i], [self.x, self.y+i*self.height, self.width, self.height])# rect(surface, color, rect, width=0)

        pygame.draw.rect(screen, WHITE, [self.x, self.y+self.focus_block*self.height, self.width, self.height], 3)

        self.fall()

    def fall(self):
        if self.y < (bottom_y[int((self.x-top_left_x)/grid_size)] - self.height * self.number):
            self.y_update_counter += 1
            if self.y_update_counter == FPS:
                self.y += grid_size
                self.y_update_counter = 0

class TargetBlock(object):
    
    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.colors = []

        self.color_set()

    def color_set(self):
        for i in range(self.number):
            random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            while random_color in self.colors:
                random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            self.colors.append(random_color)     

    def draw(self, screen):
        for i in range(self.number):
            pygame.draw.rect(screen, self.colors[i], [self.x, self.y+i*self.height, self.width, self.height])# rect(surface, color, rect, width=0)