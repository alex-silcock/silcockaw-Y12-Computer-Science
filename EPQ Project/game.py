# Ideas : Something like pipex, but a simpler version

# Check list :
# Actual Game
# Controlled by key presses
# Collisions : if something touches something = points / player dies
# Main menu
# Some sort of AI to enhance the game e.g. an AI bot playing against the person
# Networking the game across computers
# Include a high scores list - stored as a text file



# ==================================== start of program ==================================== #

# -- Library imports
import pygame

# -- Global constants, functions, procedures, classes

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (204,0,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1080, 800)
screen = pygame.display.set_mode(size)
# To make game fullscreen use this:
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# -- Title of window
pygame.display.set_caption("Game Name")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

# Set game loop to false so it runs
done = False

# Create an object using the class


# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # Clear the screen
    screen.fill(BLACK)
    

    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
    
#End While
pygame.quit()




    