import pygame

#tile class is inheriting from a class built into the pygame module
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size): #pos will be a tuple for x and y coordinates
        super().__init__()
        self.image = pygame.Surface((size,size)) #size is width and height of surface
        self.image.fill((40,12,120))
        self.rect = self.image.get_rect(topleft = pos)
        
        
    def update(self, x_shift): #x_shift is the parameter for screen scrolling camera because as your character moves from left to right it will be the x-coordinate of our screen that will need to move with him
        self.rect.x += x_shift
        