
import pygame
from pygame.locals import *
from pygame import Rect
import numpy as NumPy
from random import randint
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



class Grid_World():
    def __init__(self,game):
        self.game = game
        self.screen = game.screen     
        self.load_tileset("tileset.bmp")
        self.character = game.char
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
        
        self.tiles[self.character.x,self.character.y] = self.character.id

    def updateChar(self):

            if self.tiles[self.character.x][self.character.y-1] == TILE_ID_GRASS and self.character.y > -1:
                 self.character.y -= 1
                 time.sleep(1)
                 print("Playing Moving Forward")
                 print(self.character.y)
            elif self.tiles[self.character.x-1][self.character.y] == TILE_ID_GRASS and  self.character.x > 0:
                self.character.x -= 1
                time.sleep(1)
                print("Playing Moving LEFT")
                print(self.character.x)
            elif self.tiles[self.character.x+1][self.character.y] == TILE_ID_GRASS and  self.character.x < 10:
                self.character.x += 1
                time.sleep(1)  
                print("Playing Moving RIGHT")
                print(self.character.x)
            elif self.tiles[self.character.x][self.character.y+1] == TILE_ID_GRASS and  self.character.y < 10:
                 self.character.y += 1
                 time.sleep(1)  
                 print("Playing Moving Down")
                 print(self.character.y)
            
    def draw(self):
        # loop all tiles, and draw
        self.generateGrid()     
        for y in range( self.tiles_y ):
                for x in range( self.tiles_x ):
                    id = self.tiles[x,y]
                    dest = Rect( x * TILE_W, y * TILE_H, TILE_W, TILE_H )
                    src = Rect( id * TILE_W, 0, TILE_W, TILE_H )
                    self.screen.blit( self.tileset, dest, src )
                    
