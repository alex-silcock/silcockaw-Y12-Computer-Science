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
    def __init__(self, color, width, height, speed, lives):
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
        self.lives = lives
    #end procedure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #end procedure

    def player_set_speed(self, val):
        self.rect.x = self.rect.x + val
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > size[0] - player_width:
            self.rect.x = size[0] - player_width
    #end procedure

    def bullet_been_shot(self):
        self.player.bullet_count -= 1
    #end procedure
#end class

class Bullet(pygame.sprite.Sprite):
    # Define the constructor for Bullet
    def __init__(self, color, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([2,2])
        self.image.fill(RED)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 2
        self.bullet_count = 50
    #end procedure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #end procedure

def number_of_lives(screen):
    font = pygame.font.SysFont("arial", 30)
    text = font.render("Lives : %a" %my_player.lives, 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (100, 100)
    screen.blit(text, textRect)
#end procedure

# -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

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
bullet_group = pygame.sprite.Group()

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# Create the invaders
number_of_invaders = 50
invader_width = 10
invader_height = 10
for x in range(number_of_invaders):
    invader_speed = random.randrange(1,2)
    my_invader = Invader(BLUE, invader_width, invader_height, invader_speed)
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader) # adds it to the group of all Sprites
#Next x

# Creating the player
player_width = 10
player_height = 10
my_player = Player(YELLOW, player_width, player_height, 0, 5)
player_group.add(my_player)
all_sprites_group.add(my_player)

# Creating the bullets

bullet_count = 50
for x in range(bullet_count):
    bullets = Bullet(RED, 2)
    bullet_group.add(bullets)


while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #end if
    #next event

    # if left is pressed, then player moves left, if right is pressed, then player moves left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_player.player_set_speed(-3)
    elif keys[pygame.K_RIGHT]:
        my_player.player_set_speed(3)
    #end if

    if keys[pygame.K_UP]:
        bullet_group.draw(screen)
    # -- User inputs here
    
    
    # -- Game logic goes after this comment
    all_sprites_group.update()

    # when invader hits the player add 5 to the score
    player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True) 
    for foo in player_hit_group:
        my_player.lives -= 1
        if my_player.lives == 0:
            done = True
        #end if
    #next foo
    
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    all_sprites_group.draw(screen)
    number_of_lives(screen)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()