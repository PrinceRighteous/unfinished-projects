from email.mime import image
import pygame
from support import import_folder #only import the function you need otherwise will get pygame.display error
#CTRL + K + L minimizes methods under a class and methods/functions in general

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface): #surface parameter is our_screen/display surface, all our parameters, arguments are passed into the level.py file where our sprite group container is for this player class
        super().__init__()
        
        #character/player image animation  attributes/variables, #attributes are variables under a class, and methods are functions under a class
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15 #float/decimal number, controls the speed at which the images for the animations cycle through each other
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos) #pos will be a tuple
        
        
        #dust particles animation attributes/variables,  #attributes are variables under a class, and methods are functions under a class
        self.import_dust_run_particles()
        self.dust_frame_index= 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        
        
        
        #player movement
        self.direction = pygame.math.Vector2(0,0) #for the left or right directions and up or down when moving our character
        self.speed = 8 #for speed of movement
        self.gravity = 0.8 #float/decimal number
        self.jumpspeed = -16
        
        #player states:
        self.state = "idle" #idle by default , self.status in tutorial video
        self.facing_right = True #default direction forplayer to face, will be changed according to keyboard pressed using pygame.keys.get_pressed() method this type of keyboard pressing method isn't neccessary though we could also use the pygame.get_event type way as well.
        self.on_ground = False # the on_ variables are made to check for collisions of our players to fix origin point of our animations
        self.on_ceiling = False
        self.on_left = False #left wall
        self.on_right = False #right wall

    def import_character_assets(self): #this is all done to import the images for our animation in a quick and organized fashion
        character_path = "/home/vision16/python practice/mario style platformer/3 - Overworld/graphics/character/"
        self.animations = {"idle":[], "run":[], "jump":[], "fall":[]} #there are different folders for each animation with there animation status name
        
        for animation in self.animations.keys(): #this is a dictionary method to just retrive the keys from the key:value pair in our dictionary variable which in this case is a string:list key value pair
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path) #through this loop weare importing all of our animations and organizing them tinto our dictionary, using import folder method which is imported from the support.py file
    
    
    
    
    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('/home/vision16/python practice/mario style platformer/1 - Basic platformer/graphics/character/dust_particles/run') #using import folder method which is imported from the support.py file
        
        
        
                
            
    def animate(self): #animates the images imported from our import_character_assets method/function
        animation = self.animations[self.state] #key from our dictionary in import_character_assets
        
        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation): #this if statement makes sure we don't go past the amount of images in our list within the dictionary otherwise we would get an index error, this is why you need to use len() method to avoid this problem
            self.frame_index = 0 #returns our list back to the first image and repeats the animation
            
        image = animation[int(self.frame_index)] #int method makes variable a whole number instead of a float and the int() will round it to the nearest whole number we have to change to an int because in order to pick an item from the list we need an integar/whole number
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False) #pygame.transform.flip(image_surface,flipping the X/horizontal Boolean, flipping the Y/Vertical Boolean)
            self.image = flipped_image
        
        
        #set the rectangle: #all of these if staements help with collision glitches, these if statements ensure the image of our player is set to correctly move with our rectangle as it moves or collides with  wall, the ground, or the ceiling. this fixes most of the jumping glitches we get.
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)
            
            
    

    def get_state(self): #to get the state of our player, so that we can use these variables/attributes to effect other code
        if self.direction.y < 0:
            self.state = 'jump'
        elif self.direction.y > 1:
            self.state = 'fall'
        else:
            if self.direction.x != 0:
                self.state = 'run'
            else:
                self.state = 'idle'

        
        
    def run_dust_animation(self):
            if self.state == "run" and self.on_ground:
                self.dust_frame_index += self.dust_animation_speed
                if self.dust_frame_index >= len(self.dust_run_particles):
                    self.dust_frame_index = 0
                    
                dust_particle = self.dust_run_particles[int(self.dust_frame_index)]    #the square brackets are used to get the number/index of the image file we which to use and we use the integar/int method to turn our dust_frame_index attributes value into a whole number/integar instead of whatever it was before which was probably a float value or a string!
                
                if self.facing_right:
                    pos = self.rect.bottomleft - pygame.math.Vector2(6,10) #math.vector2 just holds a x,y value #needs to be an (x,y) coordinate and the rect bottomleft is a x,y coordinate
                    self.display_surface.blit(dust_particle, pos) #this should blit the particle animation to the player when he's running to the right, DON"T FORGET surface is our OUR_SCREEN == display screen
                    
                if not self.facing_right:
                    flipped_dust_particle = pygame.transform.flip(dust_particle,True,False)
                    pos_two = self.rect.bottomright - pygame.math.Vector2(3,2)
                    self.display_surface.blit(flipped_dust_particle, pos_two)
        
        
        
        
        
        
    def movement(self): #this function has to be run in update function or the movement code won't work, adds our movement code to keyboard buttons so that when we press the particular keyboard button the code activates
        key_pressed = pygame.key.get_pressed()
        
        if key_pressed[pygame.K_RIGHT]: #makes our character face the right direction
            self.direction.x = 1
            self.facing_right = True
        elif key_pressed[pygame.K_LEFT]: #makes our character face the left direction
            self.direction.x = -1
            self.facing_right = False
        else: #makes our character stand still
            self.direction.x = 0
            
        if key_pressed[pygame.K_SPACE]:
            self.jump()
            
            
    def apply_gravity(self):
        self.direction.y += self.gravity #makes gravity increase every single frame
        self.rect.y += self.direction.y
        
    
    def jump(self): #for our player jumping movement speed and to write the particular code needed to make sure he can jump
        if self.on_ground == True:
            self.direction.y = self.jumpspeed
        
        
    
    def update(self): #call all other methods in this one and call this method in the level.py file run method under level class
        self.movement() #this function has to be run in update function or the movement code won't work
        self.get_state()
        self.animate()
        self.run_dust_animation()
        