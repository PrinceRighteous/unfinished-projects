import os
import pygame


def import_folder(path): #regular function with regular argument that needs to be put i,
    #the argument for path will be 

    surface_list = []
   
    for _ ,__ , img_files in os.walk(path): #os.walk method mainly used in for loops, the two underscores indicate that you don't want the begining extra information/path to show in terminal
       for image in img_files:
           full_path = path + "/" + image 
           image_surf = pygame.image.load(full_path).convert_alpha()
           surface_list.append(image_surf)
        
    return surface_list
       
       
       
#print(import_folder("/home/vision16/python practice/mario style platformer/3 - Overworld/graphics/character/"))