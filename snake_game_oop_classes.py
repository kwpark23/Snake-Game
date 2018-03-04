import pygame
import random


class Snake:
    '''
    Create snake model.
    '''
    
    def __init__(self, Setting):
        '''
        @param Snake self:
        @rtype: None 
        '''
        
        self.setting = Setting
        self.lead_x = (self.setting.display_width)/2
        self.lead_y = (self.setting.display_height)/2
        self.lead_x_change = 10
        self.lead_y_change = 0
        self.snakeList = []
        self.snakeLength = 1
        self.block_size = 20
        self.snake_img = pygame.image.load('Snakehead.png')
        self.direction = 'right'
        


    def draw_snake(self, block_size, snakeList, direction):
        '''
        Creates snake head and the body.
        '''

        if direction == "up":
            head = self.snake_img
        if direction == "down":
            head = pygame.transform.rotate(self.snake_img, 180)
        if direction == "right":
            head = pygame.transform.rotate(self.snake_img, -90) 
        if direction == "left":
            head = pygame.transform.rotate(self.snake_img, 90)
        Setting().gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
        for XnY in snakeList[:-1]: 
            pygame.draw.rect(self.setting.gameDisplay, self.setting.green,  [XnY[0], XnY[1], block_size, block_size])

class Apple:
    '''
    Create apple model.
    '''
    
    def __init__(self, Setting):
        self.setting = Setting
        self.AppleThickness = 30
        self.apple_img = pygame.image.load('Apple.png')
        


    def generate_apple(self):
        '''
        Return new coordinates of an apple.
        '''
        
        randAppleX = round(random.randrange(0, self.setting.display_width - self.AppleThickness))
        randAppleY = round(random.randrange(0, self.setting.display_height - self.AppleThickness))
        return randAppleX, randAppleY



class Setting:
    '''
    Setting and controls for the game.
    '''
    
    def __init__(self):
        self.display_width = 750
        self.display_height = 500
        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        print(self.gameDisplay)
        self.white = (230, 214, 214)
        self.black = (0, 0, 0)
        self.red = (213, 27, 27)
        self.green = (27, 196, 59)
        self.orange = (224, 102, 20)
        self.yellow = (224, 221, 20)
        self.purple = (192, 66, 217)
        self.FPS = 15
        self.smallfont = pygame.font.SysFont("arial", 30)
        self.medfont = pygame.font.SysFont("arial", 50)
        self.largefont = pygame.font.SysFont("arial", 70)
        self.caption = pygame.display.set_caption('Vegan Snake')
        self.icon = pygame.display.set_icon(Apple(Setting).apple_img)
        self.update = pygame.display.update()
         

    def text_objects(self, text, color, size):
        '''
        Helper function for message_to_screen method.

        @param Setting self:
        @param str text:
        @param tup[int] color:
        @param str size:
        @rtype: Setting, Setting
        '''
        
        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = self.medfont.render(text, True, color)
        elif size == "large":
            textSurface = self.largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()


    def message_to_screen(self, text, color, y_displace=0, size='small'):
        '''
        Displays text on game screen.

        @param Setting self:
        @param str text:
        @param tup[int] color:
        @param int y_displace:
        @param str size
        @rtype: Setting
        '''
        
        textSurf, textRect = self.text_objects(text, color, size) 
        textRect.center = (self.display_width / 2), (self.display_height / 2) + y_displace
        self.gameDisplay.blit(textSurf, textRect)


    def intro_screen(self):
        '''
        Helper function for game_intro().
        '''

        self.gameDisplay.fill(self.white)
        self.message_to_screen("Welcome to Vegan Snake", self.green, -100, "large") 
        self.message_to_screen("The objective of the game is to eat red apples", self.black, -30)
        self.message_to_screen("The more apples you eat, longer you get", self.black, 10) 
        self.message_to_screen("If you run into yourself, or the edges, you die", self.black, 50) 
        self.message_to_screen("Press C to play, P to pause or Q to quit", self.red, 130)
        pygame.display.update()
        self.clock.tick()

        
    def game_intro(self):
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
            self.intro_screen()
        

    def score(self, score):
        '''
        @param int score:
        '''
        
        text = self.smallfont.render("Score: " + str(score), True, self.orange)
        self.gameDisplay.blit(text,[0,0])


    def pause(self):
        '''
        Display pause screen.
        '''

        self.gameDisplay.fill(self.purple)
        paused = True
        self.message_to_screen("Paused", self.orange, -100, "large")
        self.message_to_screen("Press C to continue or Q to quit.", self.black , 25)
        pygame.display.update()
        while paused:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.clock.tick() 



if __name__ == "__main__":
    import doctest
    doctest.testmod()



         
            
