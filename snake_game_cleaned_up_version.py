import pygame
import random



def text_objects(text, color, size):
    '''
    Helper function for message_to_screen().
    '''

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect() #get_rect() returns coordinates


def message_to_screen(message, color, y_displace=0, size="small"):
    '''
    Helper function that display text message on the specified coordinates.
    '''

    textSurf, textRect = text_objects(message, color, size) #Returns textSurface and textSurface.get_rect()
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect) #display the text on textRect position


def score(score):
    '''
    Helper function that displays score on the game screen.
    '''

    text = smallfont.render("Score: " + str(score), True, orange)
    gameDisplay.blit(text,[0,0])


def randAppleGen():
    '''
    Helper function that returns random coordinates for new apples.
    '''

    randAppleX = round(random.randrange(0, display_width - AppleThickness))
    randAppleY = round(random.randrange(0, display_height - AppleThickness))
    return randAppleX, randAppleY #Return coordinates for apple


def intro_screen():
    '''
    Helper function for game_intro().
    '''

    gameDisplay.fill(yellow)
    message_to_screen("Welcome to Vegan Snake", green, -100, size="large") #text move up from center
    message_to_screen("The objective of the game is to eat red apples", black, -30) #text move up from center
    message_to_screen("The more apples you eat, longer you get", black, 10) #text move down from center
    message_to_screen("If you run into yourself, or the edges, you die", black, 50) #text move down from center
    message_to_screen("Press C to play, P to pause or Q to quit", red, 130)
    pygame.display.update() #Update new display
    clock.tick() #Need to be called for every frame


def pause():
    '''
    Display pause screen.
    '''

    gameDisplay.fill(purple)
    paused = True
    message_to_screen("Paused", orange, -100, size = "large")
    message_to_screen("Press C to continue or Q to quit.", black , 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get(): #pygame.event.get() returns the event from the queue
            if event.type == pygame.QUIT: #pygame.QUIT is Nonetype
                pygame.quit() #Initialize the program
                quit() #Exits the program completely
            if event.type == pygame.KEYDOWN: #Detect if keyboard key is pressed down
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick() #Need to be called for every frame


def game_intro():
    '''
    Display intro screen.
    '''

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        intro_screen()


def snake(block_size, snakeList, direction):
    '''
    Control the direction of snake head.
    '''

    if direction == "up":
        head = snake_img
    if direction == "down":
        head = pygame.transform.rotate(snake_img, 180)
    if direction == "right":
        head = pygame.transform.rotate(snake_img, -90) #Rotate the object clockwise if the angle is negative
    if direction == "left":
        head = pygame.transform.rotate(snake_img, 90) #Rotate the object counterclockwise if the angle is positive
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1])) #location of the snake head
    for XnY in snakeList[:-1]: #make a rectangle on the latest coordinates next to snake head
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size]) #Make a green square


def gameLoop():
    '''
    Runs the game.
    '''

    direction = 'right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2 #375 pixel
    lead_y = display_height/2 #250 pixel
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX, randAppleY = randAppleGen() #random coordinates for the apple


    while not gameExit:
        #Game over options
        if gameOver == True:
            message_to_screen("Game Over", red, y_displace = -50, size = "large")
            message_to_screen("Press C to play again or Q to quit", black, 50, size = "small")
            pygame.display.update()
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #Moving snakes around
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)
        print('white background')
        gameDisplay.blit(apple_img, (randAppleX, randAppleY))
        print('apple generated')

        # right most edge or left most edge or bottom most edge or top most edge
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True #Game over if snake move out of screen

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        snakeHead = []
        snakeHead.append(lead_x) #Move snake head to new coordinate
        snakeHead.append(lead_y) #Move snake head to new coordinate
        snakeList.append(snakeHead) #add new coordinates to the list moves

        if len(snakeList) > snakeLength: #check if there are more than one coordinates in the list
            del snakeList[0] #Delete the oldest coordinate
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True #Game over if snake eats itself
        snake(block_size, snakeList, direction)
        score(snakeLength - 1) #Score starts at zero
        pygame.display.update()

        #The part where snake touches the apple
        if (lead_x > randAppleX and lead_x < randAppleX + AppleThickness) or \
                (lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness):
            if (lead_y > randAppleY) and (lead_y < randAppleY + AppleThickness):
                randAppleX, randAppleY = randAppleGen() #move apple to random location
                snakeLength += 1
            elif (lead_y + block_size > randAppleY) and (lead_y + block_size < randAppleY + AppleThickness):
                randAppleX, randAppleY = randAppleGen() #move apple to random location
                snakeLength += 1

        clock.tick(FPS) #Changes how fast snake moves

    pygame.quit() #When game exits, initialize the program
    quit() #exits the program



if __name__ == "__main__":
    pygame.init()
    white = (230, 214, 214)
    black = (0, 0, 0)
    red = (213, 27, 27)
    green = (27, 196, 59)
    orange = (224, 102, 20)
    yellow = (224, 221, 20)
    purple = (192, 66, 217)
    display_width = 750
    display_height = 500
    FPS = 15
    direction = "right"
    AppleThickness = 30
    block_size = 20
    smallfont = pygame.font.SysFont("arial", 30)
    medfont = pygame.font.SysFont("arial", 50)
    largefont = pygame.font.SysFont("arial", 70)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Vegan Snake')
    snake_img = pygame.image.load('Snakehead.png')
    apple_img = pygame.image.load('Apple.png')
    pygame.display.set_icon(apple_img)
    clock = pygame.time.Clock()
    game_intro() #Run intro just once at the beginning
    gameLoop()
