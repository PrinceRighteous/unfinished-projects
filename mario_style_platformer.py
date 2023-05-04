import pygame
from settings import * # * means import all from our settings.py file
from tiles import *
from level import Level  



pygame.init()
pygame.mixer.init()
CLOCK = pygame.time.Clock()



OUR_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #preferable height = 600
title = pygame.display.set_caption("mario style platformer")




#level class object/instance:
level = Level(level_map, OUR_SCREEN) #level_map from settings and our game screen/display






while True:
    CLOCK.tick(60)
               
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                
                

    OUR_SCREEN.fill((0,0,0)) #must be in the main gameloop if camera scrolling through game screen
    level.run()
    pygame.display.update()

