import pygame
from pygame.locals import *    
from pygame import Color  
from grid_world import Grid_World
from character import character

from ctypes import windll, byref,wintypes
from ctypes.wintypes import SMALL_RECT
import os
import sys

    
class Game():
    done  = False
   
    x = 510
    y = 40
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
   
    STDOUT = -11
    hdl = windll.kernel32.GetStdHandle(STDOUT)
    rect = wintypes.SMALL_RECT(0, 50, 50, 79) # (left, top, right, bottom)
    windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))
    windll.kernel32.SetConsoleCursorPosition(hdl, 0,0)
 
    
   
    
    
    def __init__(self, width=610, height=610):        
        pygame.init()
        hr = 48
        print(" "+"-"*hr+" ")
        print("|"+" "*15+"Welcome to aiRPG"+" "*15+"  |")
        print("|"+"   COS30002-Artificial Intelligence for Games"+"   |")
        print("|"+" "*17+"Created By "+" "*17+"   |")
        print("|"+" "*10+"Kaelob Smythe ( 100597078 )  "+" "*7+"  | ")
        print(" "+"-"*hr+" ")
        
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.done = False
        
        pygame.display.set_caption("aiRPG")
         ## Create the Hero, and set variables for GOAP
        self.hero = character(0,9)
        self.hero.setHP(20)
        self.hero.setDamage(4)
        self.hero.setHeal(10)
        ## Create the Enemy, and set variables for GOAP
        self.enemy = character(9,3)
        self.enemy.setHP(20)
        self.enemy.setDamage(6)
        self.enemy.setHeal(6)
        self.grid = Grid_World(self)
       
       
      


    def main_loop(self):
        
      
        
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        break # break out of the for loop
                if self.done:
                    break # to break out of the while loop
            self.draw()
            self.update()
           

    def draw(self):
        
        self.screen.fill(Color("black")) 
        self.grid.draw()   
        pygame.display.flip()
        
      
   
    def update(self):
         self.grid.updateChar(self.hero)
         self.grid.updateChar(self.enemy)
  
  


