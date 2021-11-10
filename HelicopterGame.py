import random               #For generating random numbers
import sys                  #For sys.exit to exit the program
import pygame               #import all modules of pygame
import os
from pygame.locals import *       

""" By using from pygame.locals import * you can call 
just the method name without having to append the module name """






#COLOURS with their RGB colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
pink = (139, 10, 80)
yellow = (255, 193, 37)
catedblue = (152, 245, 255)
gold = (255,215,0)
blue = (2, 128, 254)



#Global Variables for the Game
FPS = 32            # Frame Per Second 
SCREENWIDTH = 500   # Screen Width 
SCREENHEIGHT = 750  # Screen Height
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
""" this set the game window of given width and height """
GROUNDY = SCREENHEIGHT*0.9  #Base Image Y-AXIS
GAME_SPRITES = {}   # Game images Dictionary
GAME_SOUNDS = {}    # Gmae sounds Dictionary
PLAYER = "GALLERY/SPRITES/bird.png"     # Our bird is the player
BACKGROUND = "GALLERY/SPRITES/BACK2.jpg" # Our background image
PIPE = "GALLERY/SPRITES/PIPE.png"       # Our obstacles
X=0





# DISPLAY FONT

def text_screen(text, color, x, y, z):
    font = pygame.font.SysFont(" comicsansms ", z)
    screen_text = font.render(text, True, color)
    SCREEN.blit(screen_text, [x, y])


# WELCOME SCREEN
def welcomeScreen():
   
    """
    SHOWS WELCOME IMAGE ON THE SCREEN
    """
    playerx = int(SCREENWIDTH/5)    #200
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)  #325
    """ playerx and player y is the coordinates of our helicopter image   (200,325)  """

    messagex = 0
    messagey = 0
    """ messagex and messagey is the coordinates of our welcome image """

    basex = 0  # x coordinate of base (0,675)
    #GROUNDY = SCREENHEIGHT * 0.8........declare in global variables for game 
    """ basex and GROUNDY is the coordinate of our base image in background """
 
    
    while True:
        for event in pygame.event.get(): # Track all the events like mouse event keyboard event etc.
             # If user click on cross button or press the escape button , close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  
                pygame.quit()      # game will quit
                sys.exit()         # close the program

            
            # if the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_f or event.key == K_UP):  
                mainGame()
                """  return this function - means go out from this function
                 and call maingame() to go into the game for playing """
            
            else:
                
                """ Below function - set_colorkey(R, G, B)  is used to transparent the 
                given RGB colour..... this RGB will not blit on the screen of game window"""
               # GAME_SPRITES['player'].set_colorkey((255, 255, 255))
               # GAME_SPRITES['message'].set_colorkey((255, 255, 255))
              
                """ blit all the images in welcome screen 
                blit means simply showing images on game window """ 
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                SCREEN.blit(GAME_SPRITES['player'], (playerx-50 ,playery))  
                

                pygame.display.update()     # Update the game window
                FPSCLOCK.tick(FPS)          # Set or control fps for our game window 



def ExitScreen(highscore):
   
    """
    SHOWS WELCOME IMAGE ON THE SCREEN
    """
    playerx = int(SCREENWIDTH/5)    #200
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)  #325
    """ playerx and player y is the coordinates of our helicopter image   (200,325)  """

    messagex = 0
    messagey = 0
    """ messagex and messagey is the coordinates of our welcome image """

    basex = 0  # x coordinate of base (0,675)
    #GROUNDY = SCREENHEIGHT * 0.8........declare in global variables for game 
    """ basex and GROUNDY is the coordinate of our base image in background """
 
    
    while True:
        for event in pygame.event.get(): # Track all the events like mouse event keyboard event etc.
             # If user click on cross button or press the escape button , close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  
                pygame.quit()      # game will quit
                sys.exit()         # close the program

            
            # if the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE ):  
                welcomeScreen()
                """  return this function - means go out from this function
                 and call maingame() to go into the game for playing """
            
            else:
                
                """ Below function - set_colorkey(R, G, B)  is used to transparent the 
                given RGB colour..... this RGB will not blit on the screen of game window"""
               # GAME_SPRITES['player'].set_colorkey((255, 255, 255))
               # GAME_SPRITES['message'].set_colorkey((255, 255, 255))
              
                """ blit all the images in welcome screen 
                blit means simply showing images on game window """ 
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                #SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                SCREEN.blit(GAME_SPRITES['hele'], (playerx-50 ,playery-370))  
                
                SCREEN.blit(GAME_SPRITES['bullet'], (20,385))
                text_screen("SCORE "+ str(X),  gold, 40, 400,30)
                text_screen("CREDITS : Pritam Das ", yellow, 180, 700,15)
                text_screen(" CLICK SPACE BAR TO CONTINUE....", blue, 30, 600,25)

                with open("highscore.txt") as f:
                    highscore = f.read()
                SCREEN.blit(GAME_SPRITES['bullet'], (305,385))
                text_screen(" H.SCORE   " +str(highscore), gold,325,407,20)

               
                

                pygame.display.update()     # Update the game window
                FPSCLOCK.tick(FPS)          # Set or control fps for our game window 












def mainGame():

    if( not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")    
    with open("highscore.txt", "r") as k:
        highscore = k.read()

    
    score = 0
    # our player coordinates
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)  #325
    basex = 0

    # Create 3 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
 
     # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]
  

   
    playerVelY = -15         #player will go up initialy by 20
    pipeVelX = -5            # our pipe will come towards game window
    playerMaxVelY = 90       # player max velocity if uparrow key is clicked
    playerMinVelY = -8000   # player min velocity

    playerAccY = 1           # the speed which our player comes down
    playerFlapAccv = -8       # velocity of upward diresction while flapping
    playerFlapped = False     # It is true only when the bird is flapping

    #GAME LOOP
    while True:

        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_f or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()
            if event.type == KEYDOWN and (event.key == K_q):
                pipeVelX = pipeVelX -0.5
                
                    
         # this function will return true if you are crashed
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes, highscore) 
        if crashTest:
               return
        
        isCollide(playerx, playery, upperPipes, lowerPipes, highscore) 

        #check for score
        global X
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2  #TO CALCULATE MIDDLE OF PLAYER X
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2  #TO CALCULATE MIDDLE OF PLAYER X
            """ IF our player crosses the middle of its length from the middle of the pipe then score will increase """
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                X = score
                print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()
                if(score > int(highscore)):
                    highscore = score
            else:
                X = score

        """ If user press up key then player velocity must be increase """
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        """ if user clicked one time up key and release then our player is not flapped so "FALSE" """
        if playerFlapped:
            playerFlapped = False  

        """ Change in the y-axis of player if velocity get change  """
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, SCREENHEIGHT)     #GROUNDY - playery - playerHeight)


        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
            


        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if  0<upperPipes[0]['x']<(-pipeVelX)+1:    #screenwidth + 100
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
           
            

    

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))

        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()

        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

            

def getRandomPipe():
    """
    Generate position of two pipes (one straight and inverted pipe)
    for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()  #400 to get the height of the pipe
    offset = SCREENHEIGHT/3   #250 this offset is for space between pipes so that bird can go through that space 
    pipex = SCREENWIDTH+10      # 500, x axis of our both pipe (inverted and normal) are same 
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 *offset)) # offset + generate 0 to 600 
    y1 = pipeHeight - y2 +offset #400 - y2+offset
    """
    y2 and y1 are the y coordinates for our inverted and straight pipe resp.
    y1 will be negative and y2 will be more pixel than our screen height so that they blit on same x axis
    as well as different y axis...and offset is the gap between two pipes
    """
    pipe =[
        {'x' : pipex, 'y': -y1},  #upeer pipe
        {'x' : pipex, 'y' : y2}   #lower pipe
    ]
    return pipe


def isCollide(playerx, playery, upperPipes, lowerPipes, highscore):

    if playery>(GROUNDY-55) or playery<0:
        GAME_SOUNDS['hit'].play()
        ExitScreen(highscore)
        
       
        #return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()+22):
            GAME_SOUNDS['hit'].play()
            #return True
            ExitScreen(highscore)

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()+22:
            GAME_SOUNDS['hit'].play()
            ExitScreen(highscore)
           # return True

    return False



                
 

 

 # This will be the main point from where our game starts  
if __name__ == "__main__":

    pygame.init() # Intial all pygame all pygame's modules

    FPSCLOCK = pygame.time.Clock() 
    """ This function is used to create a clock object
     which can be used to keep track of time """

    pygame.display.set_caption("__HELICOPTER-GAME__")
    """ This function set the
    caption of our game window """

    GAME_SPRITES['numbers']=(
        pygame.image.load("GALLERY/SPRITES/0.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/1.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/2.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/3.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/4.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/5.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/6.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/7.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/8.png").convert_alpha(),
        pygame.image.load("GALLERY/SPRITES/9.png").convert_alpha(),
    )
    
    GAME_SPRITES['message'] = pygame.image.load("GALLERY/SPRITES/message.png").convert_alpha()

    GAME_SPRITES['base'] = pygame.image.load("GALLERY/SPRITES/base.jpg").convert_alpha()

    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),      # Rotate this image at 180 degree
        pygame.image.load(PIPE).convert_alpha()
        )
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
     # print(GAME_SPRITES['background'].get_size())

    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['hele'] = pygame.image.load("GALLERY/SPRITES/hele.png").convert_alpha()
    GAME_SPRITES['bullet'] = pygame.image.load("GALLERY/SPRITES/BULLET.png").convert_alpha()
    """ GAME_SPRITES ia a dictionary 
        IT HAS ITEMs-
        
        ITEMS     :    VALUES

        1-numbers : tuple ( jpg image from 1 to 9 )
        2-message : jpg image of starting welcome message
        3-pipe    : tuple ( inverted image of pipe and straight pipe )
        4-background : background image
        5-player : player image
        6-base : image of base background
    """


    # GAME SOUNDS
    GAME_SOUNDS["point"] = pygame.mixer.Sound("GALLERY/MUSICS/point.wav")
    GAME_SOUNDS["wing"] = pygame.mixer.Sound("GALLERY/MUSICS/wing.wav")
    GAME_SOUNDS["swoosh"] = pygame.mixer.Sound("GALLERY/MUSICS/swoosh.wav")
    GAME_SOUNDS["hit"] = pygame.mixer.Sound("GALLERY/MUSICS/hit.wav")
    GAME_SOUNDS["die"] = pygame.mixer.Sound("GALLERY/MUSICS/die.wav")

    """ GAME_SOUNDS ia a dictionary 
        IT HAS ITEMs-
        
        ITEMS     :    VALUES

        1-points    :   sound of score
        2-wing      :   sound of wings of helicopter
        3-swoosh    :   sound of swoosh 
        4-hit       :   sound of getting hit (game over)
        5-die       :   sound of die
    """
   
    while True:
        welcomeScreen() # Show welcome screen to the user untill close button is pressed
        #mainGame() # This is main game function
      


        