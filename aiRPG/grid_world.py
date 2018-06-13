
import pygame
from searches import searches
from goapInteraction import goapInteraction
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
TILE_ID_KEY = 7

graph = {'A' : ['B'],
	'B' : ['A', 'C'],
	'C' : ['B', 'D'],
	'D' : ['C', 'E'],
	'E' : ['D', 'F'],
	'F' : ['E', 'G'],
    'G' : ['F', 'H'],
	'H' : ['G', 'I'],
	'I' : ['H', 'J', 'K'],
	'J' : ['I', 'L'],
	'K' : ['I', 'L', 'N'],
	'L' : ['J', 'K', 'M'],
	'M' : ['L', 'N'],
	'N' : ['K', 'M', 'O'],
	'O' : ['N', 'P'],
	'P' : ['O', 'Q'],
	'Q' : ['P']}


class Grid_World():
    def __init__(self,game):
        self.objectobtained = False
        self.game = game
        self.screen = game.screen     
        self.load_tileset("tileset.bmp")
        self.hero = game.hero
        self.enemy = game.enemy
        self.clear()
        self.generateGrid()
        self.goap = goapInteraction(self)
       
        
        self.searches = searches()
        self.path = self.searches.shortest_path(graph,'A','Q')
        print(">> Shortest path to key found!")
        print(">> "+str(self.path))
        print(">> Following Path")
       
        
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
        if self.objectobtained == False:
            self.tiles[6,6] = TILE_ID_KEY
        if self.hero.alive:
            self.tiles[self.hero.x,self.hero.y] = TILE_ID_HERO
        if self.enemy.alive:
            self.tiles[self.enemy.x,self.enemy.y] = TILE_ID_ENEMY
        

    def updateChar(self,char):
            if not self.objectobtained:
                 self.movePlayerAlongPath(char)
                 
            else:
                self.charRandomMove(char)
          
            
               

            
            
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
        if hero.x == enemy.x and hero.y == enemy.y and hero.alive and enemy.alive:
            self.goap.run_game()
        else:
            return False

    def movePlayerAlongPath(self,char):
        
        path = self.path
        for i in range(len(self.path)):
          if path[i] == "A":
              char.x += 1
              time.sleep(0.2)
                
          elif path[i] == "B":
              char.x += 1
             
              time.sleep(0.2)
          elif path[i] == "C":
              char.x += 1
              
              time.sleep(0.2)
          elif path[i] == "D":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "E":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "F":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "G":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "H":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "I":
              char.x += 1
              time.sleep(0.2)
          elif path[i] == "K":
              char.y -= 1
              time.sleep(0.2)
          elif path[i] == "N":
              char.y -= 1
              time.sleep(0.2)
          elif path[i] == "O":
              char.x -= 1
              time.sleep(0.2)
          elif path[i] == "P":
              char.x -= 1
              time.sleep(0.2)
          elif path[i] == "Q":
              char.y -= 1
              time.sleep(0.2)
              self.objectobtained = True
              print(">> A key has been added to the heros inventory!")
    
    def charRandomMove(self,char):
        irand = randrange(0, 10)
        speed = 0
        ## Check Player can move UP without obstacle
        if char == self.hero and self.hero.alive:
            speed = 0.2
        elif char == self.enemy and self.enemy.alive:
            speed = 0.1
           
        if self.tiles[char.x][char.y-1] in (TILE_ID_GRASS,TILE_ID_ENEMY,TILE_ID_HERO) and char.y > -1 and char.previousDirection != 'DOWN' and irand in (1,2):
                char.y -= 1
                char.previousDirection = 'UP'
                time.sleep(speed)
                
               
        ## Check Player can move LEFT without obstacle
        elif self.tiles[char.x-1][char.y] in (TILE_ID_GRASS,TILE_ID_ENEMY,TILE_ID_HERO) and  char.x > 0  and char.previousDirection != 'RIGHT' and irand == 3 :
            char.x -= 1
            char.previousDirection = 'LEFT' 
            time.sleep(speed)
            
                
              
        ## Check Player can move RIGHT without obtacle
        elif self.tiles[char.x+1][char.y] in (TILE_ID_GRASS,TILE_ID_ENEMY,TILE_ID_HERO) and  char.x < 9 and irand == 5 :
            char.x += 1
            char.previousDirection = 'RIGHT'
            time.sleep(speed)  
                
               
        ## Check Player can move DOWN without obstacle
        elif self.tiles[char.x][char.y+1]in (TILE_ID_GRASS,TILE_ID_ENEMY,TILE_ID_HERO) and  char.y < 9  and irand == 7:
                char.y += 1
                char.previousDirection = 'DOWN'
                time.sleep(speed)
        if self.checkSimpleCollision(self.hero,self.enemy):
                print("Collision Detected")
        
        if self.tiles[self.hero.x][self.hero.y] == TILE_ID_EXIT and self.objectobtained:
            self.game.done = True
            print(">> The player has survived the trechourous map!")
            print(">> Game over for now!")


