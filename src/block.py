import pygame
import random
from global_info import *

width = 800
height = 600
FPS = 32
BLOCK_COLORS = [BLUE, GREEN, RED, YELLOW, PURPLE, PINK, CYAN]

class MyBlock(object):

    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.colors = []
        self.vel_x = 1
        self.vel_y = 30
        self.new_color = True
        self.focus_block = number-1#focus on bottom block

    def color_set(self):#중복되지 않도록 블록 색깔 뽑기
        for i in range(self.number):
            random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            while random_color in self.colors:
                random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            self.colors.append(random_color) 
            
    def draw(self, screen):
        if(self.new_color):
            self.color_set()
            self.new_color = False

        for i in range(self.number):
            pygame.draw.rect(screen, self.colors[i], [self.x, self.y+i*self.height, self.width, self.height])# rect(surface, color, rect, width=0)
            if(i == self.number-1):
                pygame.draw.rect(screen, WHITE, [self.x, self.y+i*self.height, self.width, self.height], 3)

        self.fall()

    def fall(self):
        if self.y < (top_left_y + play_height - self.height * self.number):
            self.y += self.vel_y

class TargetBlock(object):
    
    def __init__(self, x, y, width, height, number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.colors = []
        self.new_color = True

    def color_set(self):
        for i in range(self.number):
            random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            while random_color in self.colors:
                random_color = BLOCK_COLORS[random.randrange(0, len(BLOCK_COLORS))]
            self.colors.append(random_color)     

    def draw(self, screen):
        if(self.new_color):
            self.color_set()
            self.new_color = False

        for i in range(self.number):
            pygame.draw.rect(screen, self.colors[i], [self.x, self.y+i*self.height, self.width, self.height])# rect(surface, color, rect, width=0)