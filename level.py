import pygame
from tiles import *
from settings import *
from Player import *
from particles import particleEffects
#this file will rely on the tile file to place somethign on screen
#this file will contain level class
#the level class specifically the run object method/function will contain most of our game logic


#LEVEL SETUP:

class Level():
    def __init__(self, level_data, surface): #level_data = level_map from settings.py and surface = OUR_SCREEN 
        self.display_surface = surface #OUR_SCREEN
        self.setup_level(level_data) #level_data = level_map
        self.world_scroll = 0 #argument for x_shift in tiles.py file class update object function, this isn't needed but tutorial has it soooo
        self.current_x = 0 #hecks the collision origin point of the wall and theplayer to fix bug where player automatically glitches up a wall
        
        #dust
        self.dust_sprite = pygame.sprite.GroupSingle()
    
    
    
    def create_jump_particles(self,pos):
        jump_particle_sprite = particleEffects(pos,'jump')
        self.dust_sprite.add(jump_particle_sprite)
    
    
        
    def setup_level(self, layout): #layout will be level_data which is the level_map from settings.py
        self.tiles = pygame.sprite.Group() #object variable
        self.player = pygame.sprite.GroupSingle() #used groupsingle() because we only want a single player
       
        
        for row_index , row in enumerate(layout): #enumerate() method to find out index of rows
            for column_index, col in enumerate(row):
                if col == "X":
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y), tile_size) #object/instance of Tile class from tiles.py file
                    self.tiles.add(tile) #add method is a pygame.sprite.Sprite method or a Group() method
                #if statement to place player:
                if col == "P":
                    x = column_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x,y), self.display_surface) #object/instance of player class from player.py file
                    self.player.add(player_sprite) #add method is a pygame.sprite.Sprite method or a Group() method
    
    
    def camera_scroll(self):
        player = self.player.sprite #taken from sprite group variable
        player_x = player.rect.centerx #taken from above player variable, uses object variables from player.py file without self keyword needed by making a variable from the sprite group we put the Player class in, in the level.py file
        direction_x = player.direction.x #taken from above player variable, uses object variables from player.py file without self keyword needed by making a variable from the sprite group we put the Player class in, in the level.py file
        
        if player_x < SCREEN_WIDTH / 6 and direction_x < 0: #LEFT scroll
            self.world_scroll = 8
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH/ 7) and direction_x > 0:
            self.world_scroll = -8
            player.speed = 0
        else:
            self.world_scroll = 0
            player.speed = 8
        
        
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed #HORIZONTAL MOVEMENT of our player moved from player class
        
        for sprite in self.tiles.sprites(): #checks for horizontal collision with tiles
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True  
                    self.current_x = player.rect.left
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left   #this code is for fixing the wall glitch up
                    player.on_right = True   
                    self.curremt_x = player.rect.right    #this code is for fixing the wall glitch up
                    
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0): #this code is for fixing the wall glitch up
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0): #this code is for fixing the wall glitch up
            player.on_right = False            
                    
                    
                    
                    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity() #taken from player file to move player vertically
        
        for sprite in self.tiles.sprites(): #checks for VERTICAL collision with tiles
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 #so gravity is cancelled out otherwise rect will dissapear
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 #so when the top of your rect hits the a tile it falls down immediatly  
                    player.on_ceiling = True
                    
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
        
        
    def run(self):  # this method will contain most of game logic, and will be what we run all of our functions in and then run this function in our main game loop on our main file!!!
        #LEVEL TILES:
        self.tiles.update(self.world_scroll) #change this number for x_shift method in tiles update object function and screen scrolling direction and speed 
        self.tiles.draw(self.display_surface) #draw method is pygame method for drawing on our game screen
        self.camera_scroll()
        
        #dust_particles
        self.dust_sprite.update(self.world_shift) #pygame.sprite.update is a built in method too pygame.sprite.Sprite() class, it updates/runs in the terminal a class withing a pygame.sprite.group container like as if you were too create a regular object/variable using a class without the pygame.sprite.Sprite containers
        self.dust_sprite.draw(self.display_surface) #pygame.sprite.draw draws onto our screen the class or method/function in a pygame.sprite.Sprite group, the same way if you were too use the pygame.blit method which is actually your display name.blit((x.y) 
        
        
        
        #PLAYER
        self.player.update()
        self.horizontal_movement_collision()#no player variable name from sprite group needed because this method is made in the level class where it's being called at
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
        
        
    
