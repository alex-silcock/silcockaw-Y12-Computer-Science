# Ideas : Something like pipex, but a simpler version

# Check list :
# Actual Game
# Controlled by key presses
# Collisions : if the ball goes over the square you get points
# Main menu
# Some sort of AI to enhance the game



# ==================================== start of program ==================================== #

# -- Library imports
import pygame

# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (204,0,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# -- Title of window
pygame.display.set_caption("Game Name")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

# -- Global constants



    