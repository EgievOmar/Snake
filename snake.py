import pygame
import random
from enum import Enum
from collections import namedtuple
pygame.init()

class Direction(Enum) :
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x', 'y')

BLOCK_SIZE = 20
class SnakeGame :
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
        #init screen
        self.display = pygame.display.set_mode((self.w, self.h)) # =tuple : list filled with constant, make sure that the values doesn't changes (security)
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        #init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x - BLOCK_SIZE, self.head.y), 
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
 
        self.score = 0
        self.food = None

    def play_step(self):
        pass

if __name__ == '_main_':
    game = SnakeGame()

    while True:
        game.play_step()
    
    pygame.quit()
