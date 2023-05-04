import pygame, sys, random
#ALL INITIALIZTIONS and TIME PYGAME MODULE
pygame.init()
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()





#SURFACE/DISPLAY:

WIDTH, HEIGHT = 1200, 1000
OUR_SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
CAPTION_TITLE = pygame.display.set_caption("pong".title())
ICON_IMAGE = pygame.image.load("medicine-ball (1).png")
ICON = pygame.display.set_icon(ICON_IMAGE)



#fps:
FRAMES_PER_SECOND = 60

#color:
DEEP_SKY_BLUE = (0, 191, 255)
WHITE = (255,255,255)




#images:
BALL_IMAGE = pygame.image.load("medicine-ball (1).png")
BALL_IMAGE_TRANSFORM = pygame.transform.scale(BALL_IMAGE,(30,30))


#fonts:
FONT = pygame.font.SysFont("ArissaTypeface.ttf", 40)







# POINTS
player_1 = 0
player_2 = 0





#RECTANGLES FOR IMAGES:
BALL_RECTANGLE = pygame.Rect(600, 700, 20, 20) #x, y, width, height
LEFT_BARRIER = pygame.Rect(10, HEIGHT / 2, 10, 110)
RIGHT_BARRIER = pygame.Rect(1180, HEIGHT / 2, 10, 110)



def point_system():
    GAME_WINNING_POINTS = 5
    GAME_WINNER_1 = "PLAYER 1 WINS!!"
    GAME_WINNER_2 = "PLAYER 2 WINS"
    if BALL_RECTANGLE.x <= 0:
        player_2 + 1
    if BALL_RECTANGLE.x >= WIDTH:
        player_1 + 1
    if player_2 == GAME_WINNING_POINTS:
        pygame.time.delay(5000)
        GAME_WINNER_FONT = FONT.render(GAME_WINNER_2, 1, (0,0,0))
        OUR_SURFACE.blit(GAME_WINNER_FONT, (WIDTH/2, HEIGHT/2 - 200))
    if player_1 == GAME_WINNING_POINTS:
        pygame.time.delay(5000)
        GAME_WINNER_FONT = FONT.render(GAME_WINNER_1, 1, (0, 0, 0))
        OUR_SURFACE.blit(GAME_WINNER_FONT, (WIDTH / 2, HEIGHT / 2 - 200))
    pygame.display.update()






def ball_movement():
    global BALL_VELOCITY_X, BALL_VELOCITY_Y
    # BALL BOUNCING MOVEMENT
    BALL_VELOCITY_Y = 3
    BALL_VELOCITY_X = 3
    if BALL_RECTANGLE.bottom >= HEIGHT or BALL_RECTANGLE.top <= 0: #REVERSES THE BALL VELOCITY TO REVERSE THE BALLS DIRECTION ONCE IT BOUNCES OFF WALL
        BALL_VELOCITY_Y *= -1
    if BALL_RECTANGLE.left <= 0 or BALL_RECTANGLE.right >= WIDTH: #REVERSES THE BALL VELOCITY TO REVERSE THE BALLS DIRECTION ONCE IT BOUNCES OFF WALL
       BALL_VELOCITY_X *= -1

    BALL_RECTANGLE.x += BALL_VELOCITY_X  # ball velocity moves x axis for the rectangle
    BALL_RECTANGLE.y += BALL_VELOCITY_Y  # ball velocity moves y axis for the rectangle



        #CAN"T FIGURE OUT HOW TO MAKE THIS BALL BOUNCE!!


def movement():

    key_down = pygame.key.get_pressed()
    VEL = 5
    if key_down[pygame.K_DOWN] and RIGHT_BARRIER.y <= 900:
        RIGHT_BARRIER.y += VEL
    if key_down[pygame.K_UP] and RIGHT_BARRIER.y >= 0:
        RIGHT_BARRIER.y -= VEL
    if key_down[pygame.K_w] and LEFT_BARRIER.y >= 0:
        LEFT_BARRIER.y -= VEL
    if key_down[pygame.K_s] and LEFT_BARRIER.y <= 900:
        LEFT_BARRIER.y += VEL





def handle_collisions():
    global BALL_VELOCITY_Y, BALL_VELOCITY_X
    if BALL_RECTANGLE.colliderect(LEFT_BARRIER):
        BALL_VELOCITY_Y *= -1
    if BALL_RECTANGLE.colliderect(RIGHT_BARRIER):
        BALL_VELOCITY_Y *= -1
    if BALL_RECTANGLE.colliderect(LEFT_BARRIER):
        BALL_VELOCITY_X *= -1
    if BALL_RECTANGLE.colliderect(RIGHT_BARRIER):
        BALL_VELOCITY_X *= -1





def draw_images():
    BACKGROUND_COLOR = OUR_SURFACE.fill(WHITE)
    BALL_IMAGE_PLACEMENT = OUR_SURFACE.blit(BALL_IMAGE_TRANSFORM, (BALL_RECTANGLE.x, BALL_RECTANGLE.y))
    RIGHT_BARRIER_PLACEMENT = pygame.draw.rect(OUR_SURFACE, DEEP_SKY_BLUE, RIGHT_BARRIER)
    LEFT_BARRIER_PLACEMENT =  pygame.draw.rect(OUR_SURFACE, DEEP_SKY_BLUE, LEFT_BARRIER)
    PLAYER_1_POINT_RENDER = FONT.render("PLAYER_1: " + str(player_1), 1, (0,0,0))
    PLAYER_2_POINT_RENDER = FONT.render("PLAYER_2: " + str(player_2), 1, (0,0,0))
    PLAYER_1_POINT_PLACEMENT = OUR_SURFACE.blit(PLAYER_1_POINT_RENDER, (50,0))
    PLAYER_2_POINT_RENDER = OUR_SURFACE.blit(PLAYER_2_POINT_RENDER, (980,970))








#OUR GAME LOOP:
def main_game_loop(loop=True):
    clock.tick(FRAMES_PER_SECOND)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                sys.exit()



        draw_images()
        point_system()
        handle_collisions()
        movement()
        ball_movement()
        pygame.display.flip()







if __name__ == "__main__":
    main_game_loop()





#NEXT STEP:
# - RANDOMIZE BALL MOVEMENT FROM STARTING POINT
# -  HANDLE COLLISION OF BALL AND BARRIERS MAKE SURE BALL MOVEMENT AFTER COLLISION IS SOMEWHAT RANDOM
# - CREATE POINT BAR USING IMAGES, FONTS, AND RECTANGLES
# - ADD SOUNDS FOR WINNER, COLLISIONS, POINTS, BACKGROUND MUSIC
# - ADD FONT APPEARNCE ONCE SOMEONE WINS
# - MOVE IMPORTANT RECTANGLES THAT NEED TO REAPEAR IN ORDER FOR GAME TO WORK INTO THE MAIN_GAME_LOOP() FUNCTION SO WE CAN AUTOMATICALLY RESTART GAME BY JUST CALLING THE MAIN_GAME_LOOP() FUNCTION IN THE MAIN_GAME_LOOP() FUNCTION

#BALL IMAGE IS NOT BOUNCING OFF WALL WITH IF STATEMENT CODE FOR BALL VELOCITY, MAY HAVE TO JUST USE THE COLLIDE RECT FUNCTION TO FIX BALL BOUNCING OFF WALLS OR EDGES OF OUR_SURFACE

 #EXTRA_NOTE = BARRIERS MOVE A LITTLE FAST WHEN YOU PRESS KEYS DOWN
 #EXTRA NOTE = USE RANDOM MODULE
 #EXTRA_NOTE = IN ORDER FOR MOVEMENT TO HAPPEN YOU CAN'T MOVE A DRAWN RECTANGLE ONLY THE RECTANGLE ITSELF YOU CAN MOVE, SO YOU CAN"T MOVE A pygame.draw.rect BUT YOU CAN MOVE A pygame.Rect