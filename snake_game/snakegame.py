# import libraries
import pygame
import time
import random


snake_speed = 15

# window size which the game will be played
window_x = 500
window_y = 300

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# initialise the game
pygame.init()
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("chaitanya's snake game")

fps = pygame.time.Clock()

# snake position
snake_position = [100, 50]


snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

# fruit position
# we are gonna set randomly

fruit_position = [random.randrange(1, window_x),
                  random.randrange(1, window_y)]
fruit_spawn = True

# setting default snake direction
direction = 'RIGHT'
change_to = direction


# creating a function to track a player's score

score = 0


def show_score(choice, color, font, size):

    # create the font object
    score_font = pygame.font.SysFont(font, size)
# true shows that you are gonna implement anti-aliasing which makes sure your curves don't have the staircase effect
    score_surface = score_font.render('Score: ' + str(score), True, color)

    score_rect = score_surface.get_rect()  # cover it with a rectangle

    # displaying text
    game_window.blit(score_surface, score_rect)


def game_over():

    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render(
        "Your Score is: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()

    # setting the position of the text
    # attribute of the rect module in pygame --> midtop
    # mid position of this co-ordinate
    game_over_rect.midtop = (window_x, window_y)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()  # used to update the content on the screen

    """
    pygame.display.flip(): This function swaps the back buffer with the front buffer, making the changes visible on the screen.
    
    back buffer: This is where you perform your drawing operations. It's essentially an off-screen or hidden area where you can prepare the
    next frame of your game or application.
    
    front buffer: this is what is displayed on the screen
        
    """

    time.sleep(2)
    pygame.quit()
    quit()


# coding the main functions of the game
"""
In Pygame, pygame.event.get() is a function that retrieves a list of events from the event queue. The event queue is where
Pygame stores information about various events that occur during the program's execution, such as keyboard presses, mouse movements, window events, etc.

"""

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'

    # we don't want to directions to be executed

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'

    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10

# snake body growing mechanism


# you are basically changing the snake's body with the position, at index 0 the new position is getting inserted

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] or (snake_position[0] < fruit_position[0] < snake_position[0] + 15 and snake_position[1] < fruit_position[1] < fruit_position[1] + 15):
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()  # will only show the last element of the list (snake_body)

    if not fruit_spawn:
        fruit_position = [random.randrange(
            1, window_x), random.randrange(1, window_y)]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(game_window, white,
                     (fruit_position[0], fruit_position[1], 15, 15))

    # game over conditions
    # HITS THE MAX PREV BLOCK HORIZONTALLY
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    # HITS THE MAX PREV BLOCK VERTICALLY
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
   # if the snake touches itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)

    # refresh the screen
    pygame.display.update()

    # FPS
    fps.tick(snake_speed)
