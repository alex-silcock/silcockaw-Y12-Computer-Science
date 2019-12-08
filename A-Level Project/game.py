# Actual Game
# Controlled by key presses
# Collisions : if something touches something = points / player dies
# Main menu
# Some sort of AI to enhance the game e.g. an AI bot playing against the person
# Include a high scores list - stored as a text file



# ==================================== start of program ==================================== #

# -- Library imports
import pygame
import random

# -- Global constants

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

# Creating the sprite groups
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
bullett_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

# Create an object using the class
class Player(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self):
        # Call the sprite constructor
        super().__init__()
        self.image = pygame.image.load("invader.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = platform.rect.x
        self.rect.y = 100
        self.lives = 100
    #end procedure

    # Class methods
    def update(self):
        self.rect.x += 1
    #end procedure
#end class
class Platform(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self):
        # Call the sprite constructor
        super().__init__()
        width = random.randrange(100)
        height = 20
        self.image = pygame.Surface([width,height])
        self.image.fill(RED)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 780
    #end procedure
#end class


player = Player()
player_group.add(player)
all_sprites_group.add(player)

for x in range(10):
    platform = Platform()
    platform_group.add(platform)
    all_sprites_group.add(platform)


# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event



    all_sprites_group.update()
    # Clear the screen
    screen.fill(BLACK)
    all_sprites_group.draw(screen)
    

    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
#End While

pygame.quit()




    