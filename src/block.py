import pygame
import random
from global_info import *

width = 800
height = 600
FPS = 32
BLOCK_COLORS = [BLUE, GREEN, RED, YELLOW, PURPLE, ORANGE, CYAN]

class MyBlock(object):

    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.colors = []
        self.vel_x = 1
        self.vel_y = 10
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
            self.y += self.vel_y

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