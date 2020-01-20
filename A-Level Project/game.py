# Controlled by key presses
# Collisions : points / player dies, could include coins to increase score, level only complete until all coins collected
# Main menu
# Some sort of AI to enhance the game e.g. an AI bot playing against the person
# Include a high scores list - stored as a JSON file
# Hardest level which includes gravity and platforms
# Textured platforms, players
# Include background music
# Timer
# Balls moving in a circle around a player, moving randomly around the screen 



# ==================================== start of program ==================================== #

# -- Library imports
import pygame, random, json

# -- Global constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
LIGHTGREEN = (100,255,100)
LIGHTBLUE = (100,100,255)
coloursList = [BLACK, WHITE, BLUE, YELLOW, RED, LIGHTGREEN, LIGHTBLUE]

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1300, 800)
screen = pygame.display.set_mode(size)
# To make game fullscreen use this:
#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

# -- Title of window
pygame.display.set_caption("Game Name")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    clock.tick(60) 
pygame.quit()






    