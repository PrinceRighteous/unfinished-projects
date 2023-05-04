import pygame, sys, random
pygame.init()
pygame.font.init()
pygame.mixer.init()


#MAKE LIST OF DIFFERENT ROCK IMAGES, ROCK EXPLOSION IMAGES, AND COORDINATES TO USE RANDOMLY TO DROP ON OUR SKELETON GAME


class Rocks():
    def __init__(self, rock_img, blue_fire_img, yellow_fire_img, coordinates_x, coordinates_y, blue_rock_explosions, yellow_rock_explosions):
        self.x = coordinates_x
        self.y = coordinates_y
        self.blue_fire_img = blue_fire_img
        self.yellow_fire_img = yellow_fire_img
        self.rock_img = random.choice(rock_img)
        self.ROCK_RECTANGLES_list = [self.rock_img.get_rect(center = (random.choice(self.x), random.choice(self.y))),self.rock_img.get_rect(center = (random.choice(self.x), random.choice(self.y))),self.rock_img.get_rect(center = (random.choice(self.x), random.choice(self.y))),
                                self.rock_img.get_rect(center=(random.choice(self.x), random.choice(self.y))),self.rock_img.get_rect(center = (random.choice(self.x), random.choice(self.y))), self.rock_img.get_rect(center = (random.choice(self.x), random.choice(self.y)))]
        self.ROCK_RECTANGLES = [self.ROCK_RECTANGLES_list[0], self.ROCK_RECTANGLES_list[1], self.ROCK_RECTANGLES_list[2], self.ROCK_RECTANGLES_list[3],
                                self.ROCK_RECTANGLES_list[4], self.ROCK_RECTANGLES_list[5]]
        self.BLUE_ROCK_EXPLOSIONS = blue_rock_explosions
        self.YELLOW_ROCK_EXPLOSIONS = yellow_rock_explosions
        self.speeds = [6, 3, 10, 9, 8, 7, 6, 13, 12, 20, 18, 15] #SPEEDS FOR FALLING ROCKS
        self.blue_fire_frames = 0
        self.yellow_fire_frames = 0
        self.loop = True



    def draw_rock(self): #blit rock to screen randomly here #while loop is making our character not be able to move
        #in order to remove blitted images you must remove the rectangle itself and the image will go with the rectangle
            for r in self.ROCK_RECTANGLES:
                OUR_SCREEN.blit(self.rock_img, (self.ROCK_RECTANGLES[0].x, self.ROCK_RECTANGLES[0].y))
                self.ROCK_RECTANGLES[0].y += self.speeds[1]
                if self.ROCK_RECTANGLES[0].y >= 600:
                    self.ROCK_RECTANGLES.remove(r)
        #for t in self.ROCK_RECTANGLES:
                #OUR_SCREEN.blit(self.rock_img, (self.ROCK_RECTANGLES[0].x, self.ROCK_RECTANGLES[0].y))
                #self.ROCK_RECTANGLES[0].y += self.speeds[1]
                #if self.ROCK_RECTANGLES[0].y >= 600:
                    #self.ROCK_RECTANGLES.remove(t)


                pygame.display.update()





    def draw_fire(self): #idk if we need this yet maybe for fire
        pass










CLOCK = pygame.time.Clock()



WIDTH, HEIGHT = 1200, 700
OUR_SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

#COLOR:
OUR_SCREEN.fill((150,20,120))


#GAME_LOGO AND TITLE/CAPTION:
icon = pygame.display.set_icon(pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turqouise_head.png"))
caption_title = pygame.display.set_caption("OH SKELETON!!")





#RANDOM STARTING COORDINATES FOR FALLING ROCKS:
COORDINATES_X = [1000, 100, 250, 320, 480, 790, 135, 465, 700, 985, 1025, 639, 676, 432, 549, 960, 234, 190, 800, 844, 266]
COORDINATES_Y = [-50, -100]


#ALL IMAGES:
#ALL SKELETON IMAGES ARE CROPPED AT 55x55:
CAVE_BACKGROUND = pygame.image.load("/home/vision16/Documents/images/cave background/cave backgrounds/undead cave/undead cave.jpg")
CAVE_BACKGROUND_TRANSFORMED = pygame.transform.scale(CAVE_BACKGROUND, (WIDTH, HEIGHT))
SKELETON_IDLE_IMAGE = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquiose_skeleton_standing.png")
SKELETON_STANDING_RIGHT = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_standing_right.png")
SKELETON_MOVING_RIGHT_1 = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_moving_right_1.png")
SKELETON_MOVING_RIGHT_2 = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_moving_right_2.png")
SKELETON_STANDING_LEFT = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_standing_left.png")
SKELETON_MOVING_LEFT_1 = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_moving_left_1.png")
SKELETON_MOVING_LEFT_2 = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /turquoise_skeleton_movements/turquoise_skeleton_moving_left_2.png")
SKELETON_IMAGES_TRANSFORMED = [pygame.transform.scale2x(SKELETON_IDLE_IMAGE),pygame.transform.scale2x(SKELETON_STANDING_RIGHT),pygame.transform.scale2x(SKELETON_MOVING_RIGHT_1)
                               ,pygame.transform.scale2x(SKELETON_MOVING_RIGHT_2),pygame.transform.scale2x(SKELETON_STANDING_LEFT),pygame.transform.scale2x(SKELETON_MOVING_LEFT_1),
                               pygame.transform.scale2x(SKELETON_MOVING_LEFT_2)]



#SOME ROCK IMAGES HAVE CROPPED WIDTH AND HEIGHT NUMBER ATTACHED TO NAME OF IMAGE
#ROCK IMAGES, FIRE, AND EXPLOSION ANIMATIONS:
FALLING_ROCKS = [pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 1/1rock1157x1158.png").convert_alpha(),pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 1/2rock1157x1157.png").convert_alpha(),
                pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 1/3rock1157x1158.png").convert_alpha(), pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 1/4rock1157x1158.png").convert_alpha(), pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 1/5rock1157x1158.png").convert_alpha(),
                 pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 2/rock1_1158x1158.png").convert_alpha(), pygame.image.load("/home/vision16/Documents/images/Rocks/rocks 2/rock2_1288x1287.png").convert_alpha()]
BLUE_FIRE_ANIMATION = [pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 1/fire10.png"), pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 1/fire11.png"),
                       pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 1/fire12.png"), pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 1/fire13.png")]
YELLOW_FIRE_ANIMATION = [pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire1.png"),pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire2.png"),pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire3.png"),
                         pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire3.png"), pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire4.png"),
                         pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire5.png"), pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire6.png"),
                         pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire7.png"),pygame.image.load("/home/vision16/Documents/images/Fire/fire animation 3/yellowfire8.png")]
BLUE_EXPLOSION_ANIMATION = [pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_1.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_2.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_3.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_4.png"), pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_5.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_6.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_7.png"), pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_8.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_9.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_10.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_11.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_12.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_13.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_14.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_15.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_16.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_17.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_18.png"),
                           pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 3/15 EXPLOSION_PNG SEQUENCE/explosion_1/explosion_19.png")]
YELLOW_EXPLOSION_ANIMATION = [pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion1.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion2.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion3.png"),
                              pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion4.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion5.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion6.png"),
                              pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion7.png"),pygame.image.load("/home/vision16/Documents/images/exsplsions/exsplosion 4/explosion8.png")]


#TRANSFORMED IMAGES AND ANIMATIONS:
TRANSFORMED_FALLING_ROCKS = [pygame.transform.scale(FALLING_ROCKS[0], (100,100)), pygame.transform.scale(FALLING_ROCKS[1], (100,100)), pygame.transform.scale(FALLING_ROCKS[2], (100,100)),
                             pygame.transform.scale(FALLING_ROCKS[3], (100,100)), pygame.transform.scale(FALLING_ROCKS[4], (100,100)), pygame.transform.scale(FALLING_ROCKS[5], (100,100)),
                             pygame.transform.scale(FALLING_ROCKS[6], (100,100))]











#MOVEMENT IMAGES:
SKELETON_RIGHT_MOVEMENTS = [SKELETON_IMAGES_TRANSFORMED[2],SKELETON_IMAGES_TRANSFORMED[3],SKELETON_IMAGES_TRANSFORMED[1]]
SKELETON_LEFT_MOVEMENTS = [SKELETON_IMAGES_TRANSFORMED[5],SKELETON_IMAGES_TRANSFORMED[6],SKELETON_IMAGES_TRANSFORMED[4]]
SKELETON_IDLE = [SKELETON_IMAGES_TRANSFORMED[0]]



#MOVEMENT BOOLEAN VARIABLES:
isjump = False
jumpcount = 10

left = False
right = False
standing_right = False
standing_left = False
idle = False
walkcount = 0







#RECTANGLE FOR SKELETON:
SKELETON_RECTANGLE = pygame.Rect(600,490,55,55)



def movement():
    global jumpcount, isjump, left, right, standing_right, standing_left
    key_pressed = pygame.key.get_pressed()


    # movement using keys:
    if key_pressed[pygame.K_RIGHT] and SKELETON_RECTANGLE.x <= 1115:
        SKELETON_RECTANGLE.x += 10
        right = True
        left = False
        idle = False
        standing_right = True
        standing_left = False
    elif key_pressed[pygame.K_LEFT] and SKELETON_RECTANGLE.x >= -30:
        SKELETON_RECTANGLE.x -= 10
        right = False
        left = True
        idle = False
        standing_right = False # won't work becasue variable will only vhange when it's pressed
        standing_left = True
    elif left == False and right == False:  # won't work becasue variable will only vhange when it's pressed
        if standing_right == True:
            idle = True
            walkcount = 0
        elif standing_left == True:
            idle = True
            walkcount = 0
    else:
        left = False
        right = False
        standing_right = False
        standing_left = False
        idle = True
        walkcount = 0


    if not(isjump):
        if key_pressed[pygame.K_SPACE] and SKELETON_RECTANGLE.y <= 490:
            isjump = True
            left = False
            right = False
            walkcount = 0

        elif key_pressed[pygame.K_SPACE] and key_pressed[pygame.K_RIGHT] and SKELETON_RECTANGLE.y <= 490:
            isjump = True
            right = True
            left = False
            walkcount = 0
        elif key_pressed[pygame.K_SPACE] and key_pressed[pygame.K_LEFT] and SKELETON_RECTANGLE.y <= 490:
            isjump = True
            left = True
            right = False
            walkcount = 0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            SKELETON_RECTANGLE.y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isjump = False
            SKELETON_RECTANGLE.y = 490
            jumpcount = 10










    
        
        




def draw_on_screen(): #value
    global walkcount #since we will be redefining in this function we make it global so it can still be recognized outside
    cave_background_placement = OUR_SCREEN.blit(CAVE_BACKGROUND_TRANSFORMED, (0, 0))
    if walkcount + 1 >= 9: #since we only have 3 images in our list and we want to show each image for 3 frames we have to make sure the walkcount won't go above 9 when we blit each image for 3 frames by doing integar division on the walkcount.
        walkcount = 0 #if doing a different animation you can change walk count variable NAME TO A DIFFERENT NAME LIKE SPRITE_ANIMATION_LIST LIMIT OR IF YOUR GONNA DO THE SAME SORT OF MCODE FOR EXSLPOSIONS YOU CAN DO EXSPLSION_COUNT

    if left:
        OUR_SCREEN.blit(SKELETON_LEFT_MOVEMENTS[walkcount//3], (SKELETON_RECTANGLE.x, SKELETON_RECTANGLE.y)) #the //3 is integar divison it ensures that theres no decimals or float numbers for the walkcount
        walkcount += 1

    elif right:
        OUR_SCREEN.blit(SKELETON_RIGHT_MOVEMENTS[walkcount//3], (SKELETON_RECTANGLE.x, SKELETON_RECTANGLE.y)) #the //3 is integar divison it ensures that theres no decimals or float numbers for the walkcount
        walkcount += 1
    elif idle == True and standing_right == True:
        OUR_SCREEN.blit(SKELETON_RIGHT_MOVEMENTS[2], (SKELETON_RECTANGLE.x, SKELETON_RECTANGLE.y))
    elif idle == True and standing_left == True:
        OUR_SCREEN.blit(SKELETON_LEFT_MOVEMENTS[2], (SKELETON_RECTANGLE.x, SKELETON_RECTANGLE.y))
    else:
        OUR_SCREEN.blit(SKELETON_IDLE[0], (SKELETON_RECTANGLE.x, SKELETON_RECTANGLE.y))
    pygame.display.update()




#OCJECT/INSTANCE for Rocks class:
ROCKY = Rocks(TRANSFORMED_FALLING_ROCKS, BLUE_FIRE_ANIMATION, YELLOW_FIRE_ANIMATION, COORDINATES_X, COORDINATES_Y, BLUE_EXPLOSION_ANIMATION,YELLOW_EXPLOSION_ANIMATION)










#MAIN GAME LOOP:
while True:
    CLOCK.tick(60) #FPS , SET TO 30 fps TEST ANIMATION

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    draw_on_screen()
    movement()
    ROCKY.draw_rock()
    pygame.display.update()
















#WHERE I LEFT OFF:
    #BLIT IN EXPLOSION WHEN ROCK HITS GROUND, BLIT IN DEATH ANIMATION IF ROCK COLLIDES WITH CHARACTER, MAKE SCREEN SHAKE WHEN ROCK HITS GROUND, FROM SKY AFTER THAT CREATE TIMER AND START SCREEN!!
    #NEED TO MAKE SURE ROCKS ARE BLITTED ON SCREEN CONTINOUSLY
    #GET RID OF BACKGROUNDS ON ROCK IMAGES
    #WORK ON attching fire to rock rectangle, and then ANIMATION FOR FIRE, and will probably have to transform fire images too







#HOW TO CROP PARTS FO A IMAGE OUT INCASE YOU HAVE A SPRITE SHEET OF PIXEL ANIMATIONS:

#SKELETON_SPRITE_SHEET = pygame.image.load("/home/vision16/Documents/images/pixel skeleton /SMB_Base_S_Tone07.png").convert_alpha()
#SKELETON_SPRITE_SHEET_TRANSFORMED = pygame.transform.scale(SKELETON_SPRITE_SHEET, (100,100))
#SKELETON_SPRITE_SHEET_RECTANGLE = SKELETON_SPRITE_SHEET_TRANSFORMED.get_rect(center = (600,550))


# FUNCTION FOR EXTRACTING PIECES OF SPRITE SHEET IMAGE:
# def get_image(sheet, width, height): #THIS FUNCTION IS THE PYTHON VERSION OF CROPPING A PIECE OF A PHOTO
# image = pygame.Surface((width,height)).convert_alpha()
# image_doubled = pygame.transform.scale2x(image)
# idle_image = image_doubled.blit(sheet, (0,0), (63,63, width, height)) #SURFACE.blit(image,(x,y), (x,y, width, height)) image, placement_coordinate, area_and_size_of_part_of_the_image_you_want_to_crop
# BLITTING sprite sheet onto surface
# return image


# VARIABLE FOR CALLING GET_IMAGE FUNCTION:
# skeleton_surfaces = [get_image(SKELETON_SPRITE_SHEET, 45, 60)]

#sprite_sheet_placement = OUR_SCREEN.blit(skeleton_surfaces[0], (0,0)) #blitting surface onto screen




#def draw_animation(skele_rectangle,move_idle,value, right_movements): #value
    #key_pressed = pygame.key.get_pressed()
    #if move_idle == False:
        #OUR_SCREEN.blit(SKELETON_IMAGES_TRANSFORMED[0],(skele_rectangle.x, skele_rectangle.y))
    #if key_pressed[pygame.K_RIGHT] and SKELETON_RECTANGLE.x <= 1100:
        #move_idle = True
        #for val in value:
           # right_movements[1:3]
            #skele_rectangle.x += 1


    #pygame.display.update()



    #goes under main game loop:
        #draw_animation(SKELETON_RECTANGLE, moving_for_idle, movement_value, ALL_RIGHT_MOVEMENTS)













#EXAMOLE OF SPRITE CLASS