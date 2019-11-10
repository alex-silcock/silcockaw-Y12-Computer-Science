import pygame
import random
import math

# -- Global Constants

## -- Define the class Invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = speed
    #End Procedure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #end proc
#End Class

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = size[0] // 2
        self.rect.y = size[1] - height
        self.speed = speed
    #end func

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #end func
#end class

# -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Invader")

# -- Exit game flag set to false
done = False

# Create a list of the invaders
invader_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# Create the invaders
number_of_invaders = 10
for x in range (number_of_invaders):
    my_invader = Invader(BLUE, 10, 10, 1)
    invader_group.add (my_invader)
    all_sprites_group.add (my_invader) # adds it to the group of all Sprites
#Next x

# Creating the player
my_player = Player(YELLOW, 10, 10, -1)
player_group.add (my_player)
all_sprites_group.add (my_player)

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - any key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
            elif event.type == pygame.KEYUP: # - any key released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.player_set_speed(0) # speed set to 0
                #end if
            #end if
        #end if
    #next event

    # -- Game logic goes after this comment
    all_sprites_group.update()
    # when invader hits the player add 5 to the score
    player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True)

    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()