import pygame
from pygame.locals import *    
from pygame import Color  
from grid_world import Grid_World
from character import character


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
    
class Game():
    done  = False
    
    def __init__(self, width=610, height=610):        
        pygame.init()
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("aiRPG")
        self.hero = character(0,9)
        self.enemy = character(1,1)
        self.grid = Grid_World(self)


    def main_loop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        break # break out of the for loop
                    if done:
                        break # to break out of the while loop
            self.update()
            self.draw()

    def draw(self):
       
        self.screen.fill(Color("black")) 
        self.grid.draw()   
        pygame.display.flip()
   
    def update(self):
         self.grid.updateChar(self.hero)
         self.grid.updateChar(self.enemy)

