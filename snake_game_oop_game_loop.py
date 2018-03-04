from snake_game_oop import Snake, Apple, Setting
import pygame


def game_loop(setting):
    '''
    Run snake game.
    '''

    #Initialize the game when it restarts
    snake.direction = 'right'
    snake.lead_x = (setting.display_width)/2 #375 pixel
    snake.lead_y = (setting.display_height)/2 #250 pixel
    snake.lead_x_change = 10
    snake.lead_y_change = 0
    snake.snakeList = []
    snake.snakeLength = 1
    randAppleX, randAppleY = apple.generate_apple() #Starting coordinates

    gameExit = False
    gameOver = False

    #Game Over Option
    while not gameExit:
        if gameOver == True:
            setting.message_to_screen("Game Over", setting.red, -50, "large")
            setting.message_to_screen("Press C to play again or Q to quit", setting.green, 50, "small")
            #pygame.display.update()
            setting.update
            print('game over')
            
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
                        game_loop() #Working
           
        #Move snake around
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.direction = 'left'
                    snake.lead_x_change = -snake.block_size
                    snake.lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake.direction = 'right'
                    snake.lead_x_change = snake.block_size
                    snake.lead_y_change = 0
                elif event.key == pygame.K_UP:
                    snake.direction = 'up'
                    snake.lead_y_change = -snake.block_size
                    snake.lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'down'
                    snake.lead_y_change = snake.block_size
                    snake.lead_x_change = 0
                elif event.key == pygame.K_p:
                    setting.pause()
    
        setting.gameDisplay.fill(setting.white)
        print('white background')
        setting.gameDisplay.blit(apple.apple_img, (randAppleX, randAppleY))
        print('apple generated')

        #Game Over when snake hits edges
        if snake.lead_x >= setting.display_width or snake.lead_x < 0 or\
           snake.lead_y >= setting.display_height or snake.lead_y < 0:
            gameOver = True

        snake.lead_x += snake.lead_x_change
        snake.lead_y += snake.lead_y_change

        snakeHead = []
        snakeHead.append(snake.lead_x)
        snakeHead.append(snake.lead_y)
        snake.snakeList.append(snakeHead)
        print('snake created')

        if len(snake.snakeList) > snake.snakeLength:
            del snake.snakeList[0]
        for nextSegment in snake.snakeList[:-1]:
            if nextSegment == snakeHead:
                gameOver = True

        snake.draw_snake(snake.block_size, snake.snakeList, snake.direction)
        setting.score(snake.snakeLength - 1)
        setting.update

        if (snake.lead_x > randAppleX and\
            snake.lead_x < randAppleX + apple.AppleThickness) or\
            (snake.lead_x + snake.block_size > randAppleX and\
             snake.lead_x + snake.block_size < randAppleX + apple.AppleThickness):
            if (snake.lead_y > randAppleY) and\
               (snake.lead_y < randAppleY + apple.AppleThickness):
                randAppleX, randAppleY = apple.generate_apple()
                snake.snakeLength += 1
            elif (snake.lead_y + snake.block_size > randAppleY) and\
                 (snake.lead_y + snake.block_size < randAppleY + apple.AppleThickness):
                randAppleX, randAppleY = apple.generate_apple()
                snake.snakeLength += 1

        setting.clock.tick(setting.FPS)

    pygame.quit()
    quit()

if __name__ == '__main__':
    pygame.init()
    setting = Setting()
    apple = Apple(setting)
    snake = Snake(setting)
    setting.caption #worked
    setting.icon #worked
    setting.game_intro() #worked 
    game_loop(setting)
