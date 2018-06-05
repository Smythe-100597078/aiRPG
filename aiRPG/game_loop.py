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
        self.char = character()
        self.grid = Grid_World(self)


    def main_loop(self):
             
        while not self.done:
            self.char.update()
            self.draw()
           
            self.clock.tick(60)
           

    def draw(self):
       
        self.screen.fill(Color("black")) 
        self.grid.draw()   
        pygame.display.flip()
