import pygame
from support import import_folder

class particleEffects(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            self.frames = import_folder("/home/vision16/python practice/mario style platformer/1 - Basic platformer/graphics/character/dust_particles/jump")
        if type == 'land':
            self.frames = import_folder("/home/vision16/python practice/mario style platformer/1 - Basic platformer/graphics/character/dust_particles/land")
        self.image = self.frames[self.frame_index] #we do not need to put our attribute/variable in the parameter if the attributes value is not being taken from an outside source/ the value isn't an function argument or parameter argument.
        self.rect = self.image.get_Rect(center = pos) #center is an x,y coordinate
        
        
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill() #function that may or may not be imported from the pygame.sprite.Sprite class i don't know but it kills the whole sprite!
        else:
            self.image = self.frames[int(self.frame_index)]
        
    def update(self, x_shift): #world_scroll is the same parameter as x_shift, these parameters are used to move the display screen from left to right when our character or particles are moving off screen
        self.animet()
        self.rect.x += x_shift #moves screen with particles, self.rect is the same Attribute/variable in our init function