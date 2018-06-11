
import pygame
from pygame.locals import *
from pygame import Rect
import numpy as NumPy
from random import randint, randrange
import os
import time


TILE_W = 61
TILE_H = 61
TILE_ID_CORNER = 0
TILE_ID_EXIT = 1
TILE_ID_GRASS = 2
TILE_ID_HERO = 3
TILE_ID_WALL = 4
TILE_ID_TREE = 5
TILE_ID_ENEMY = 6


class Grid_World():
    def __init__(self,game):
        self.game = game
        self.screen = game.screen     
        self.load_tileset("tileset.bmp")
        self.hero = game.hero
        self.enemy = game.enemy
        self.clear()
        self.generateGrid()
        
    def load_tileset(self, image="tileset.bmp"):        
        self.tileset = pygame.image.load(os.path.join("images", image)).convert()
        self.rect = self.tileset.get_rect()
        
    def clear(self):
        self.tiles_x, self.tiles_y = 60, 40
        ## Fill the Grid World with Grass = TILE_ID_GRASS == 2
        self.tiles = NumPy.full( (self.tiles_x, self.tiles_y ), 2)        
      
    def generateGrid(self):
       
        
        for i in range(8, 3, -1):
            self.tiles[0,i] = TILE_ID_TREE
        self.tiles[0,1] = TILE_ID_TREE
        self.tiles[0,0] = TILE_ID_CORNER
        for i in range(1, 9):
            self.tiles[i,0] = TILE_ID_WALL
        self.tiles[9,0] = TILE_ID_EXIT
        for i in range(1, 7):
            self.tiles[i,2] = TILE_ID_TREE
        for i in range(5, 10):
            self.tiles[i,5] = TILE_ID_TREE
        for i in range(6, 8):
            self.tiles[4,i] = TILE_ID_TREE
        for i in range(5, 8):
            self.tiles[i,8] = TILE_ID_TREE
        for i in range(0,10):
            for j in range(0,10):
                if self.tiles[i,j] != TILE_ID_TREE and self.tiles[i,j] != TILE_ID_CORNER and self.tiles[i,j] != TILE_ID_EXIT and self.tiles[i,j] != TILE_ID_WALL:
                    self.tiles[i,j] = TILE_ID_GRASS
        
        self.tiles[self.hero.x,self.hero.y] = TILE_ID_HERO
        self.tiles[self.enemy.x,self.enemy.y] = TILE_ID_ENEMY

    def updateChar(self,char):
            irand = randrange(0, 10)
            speed = 0
            ## Check Player can move UP without obstacle
            if char == self.hero:
                speed = 0.5
            elif char == self.enemy:
                speed = 0.1
           
            if self.tiles[char.x][char.y-1] == TILE_ID_GRASS and char.y > -1 and char.previousDirection != 'DOWN' and irand in (1,2):
                 char.y -= 1
                 char.previousDirection = 'UP'
                 time.sleep(speed)
                
               
            ## Check Player can move LEFT without obstacle
            elif self.tiles[char.x-1][char.y] == TILE_ID_GRASS and  char.x > 0  and char.previousDirection != 'RIGHT' and irand == 3 :
                char.x -= 1
                char.previousDirection = 'LEFT' 
                time.sleep(speed)
            
                
              
            ## Check Player can move RIGHT without obtacle
            elif self.tiles[char.x+1][char.y] == TILE_ID_GRASS and  char.x < 9 and irand == 5 :
                char.x += 1
                char.previousDirection = 'RIGHT'
                time.sleep(speed)  
                
               
            ## Check Player can move DOWN without obstacle
            elif self.tiles[char.x][char.y+1] == TILE_ID_GRASS and  char.y < 9  and irand == 7:
                 char.y += 1
                 char.previousDirection = 'DOWN'
                 time.sleep(speed)
            
            if self.checkSimpleCollision(self.hero,self.enemy):
                print("Collision Detected")
               
            
    def draw(self):
        # loop all tiles, and draw
        self.generateGrid()     
        for y in range( self.tiles_y ):
                for x in range( self.tiles_x ):
                    id = self.tiles[x,y]
                    dest = Rect( x * TILE_W, y * TILE_H, TILE_W, TILE_H )
                    src = Rect( id * TILE_W, 0, TILE_W, TILE_H )
                    self.screen.blit( self.tileset, dest, src )


    def checkSimpleCollision(self,hero,enemy):
        if hero.x == enemy.x and hero.y == enemy.y:
            return True
        else:
            return False
                    
