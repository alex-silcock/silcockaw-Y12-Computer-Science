import pygame
import random

my_map =[['h','h','h','h','h','h','h','h','h','h'],
        ['v',  0,  0,  0,  0,  0,  0,  0,  0, 'v'],
        ['v',  0,  0,  0,  0,  0,  0,  0,  0, 'v'],
        ['v', 'h', 0, 'h','h','h','h','h', 0, 'v'],
        ['v',  0,  0,  0,  0,  0, 'v', 0,  0, 'v'],
        ['v',  0, 'v','h','v', 0, 'v', 0,  0, 'v'],
        ['v',  0, 'v','v','v', 0, 'v', 0,  0, 'v'],
        ['v',  0, 'v','h','v', 0, 'v', 0,  0, 'v'],
        ['v',  0,  0,  0,  0,  0,  0,  0,  0, 'v'],
        ['h', 'h','h','h','h','h','h','h','h','h']]
        
#h = horizontal wall
#v = vertical wall

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# -- Title of window
pygame.display.set_caption("Maps")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

# Set game loop to false so it runs
done = False

## -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

## -- Define the class tile which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor for the tile
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure
#end class

## -- Define the class for the player
class Player(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create the sprite
        width = 10
        height = 10
        color = RED
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure

    # Class methods
    def player_update_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val
    #end procedure
#end class

## -- Define the class for the the things to be eaten
class OtherPlayer(pygame.sprite.Sprite):
    # Define the constructor
    def __init__(self, x_ref, y_ref, x_speed, y_speed):
        # Call the sprite constructor
        super().__init__()
        # Create the sprite
        width = 5
        height = 5
        color = YELLOW
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        
        self.speed_x = x_speed
        self.speed_y = y_speed
    #end procedure

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #end if
    #end procedure
#end class


# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# Create a list of tiles for the walls
wall_group = pygame.sprite.Group()
vertical_wall_group = pygame.sprite.Group()
horizontal_wall_group = pygame.sprite.Group()

# Create a list of other players
otherplayer_group = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range(10):
        if my_map[x][y] == 'v':
            my_wall = Tile(BLUE, 20, 20, x*20, y*20)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
            vertical_wall_group.add(my_wall)
        elif my_map[x][y] == 'h':
            my_wall = Tile(BLUE, 20, 20, x*20, y*20)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
            horizontal_wall_group.add(my_wall)
        #end if
    #next x
#next y

pacman = Player(20, 20)
all_sprites_group.add(pacman)

computerPlayer = OtherPlayer(40, 60, 1, 1)
all_sprites_group.add(computerPlayer)
otherplayer_group.add(computerPlayer)

# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.player_update_speed(-2, 0)
    elif keys[pygame.K_RIGHT]:
        pacman.player_update_speed(2, 0)
    elif keys[pygame.K_UP]:
        pacman.player_update_speed(0, -2)
    elif keys[pygame.K_DOWN]:
        pacman.player_update_speed(0, 2)
    #end if 

    # -- Check for collisions between pacman and wall tiles
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_group, False)
    player_hit_otherplayer_list = pygame.sprite.spritecollide(pacman, otherplayer_group, True)
    if len(player_hit_otherplayer_list) > 0:
        computerPlayer = OtherPlayer(40, 40, 1, 1)
        all_sprites_group.add(computerPlayer)
        otherplayer_group.add(computerPlayer)
    #end if

    for foo in player_hit_list:
        pacman.player_update_speed(0, 0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y
        # Run the update function for all sprites
    #next foo
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y

    computerPlayer_vertical_wall_list = pygame.sprite.spritecollide(computerPlayer, vertical_wall_group, False)
    computerPlayer_horizontal_wall_list = pygame.sprite.spritecollide(computerPlayer, horizontal_wall_group, False)

    #if the wall is vertical or horizontal, the collisions would be different for each wall
    if len(computerPlayer_vertical_wall_list) > 0:
        computerPlayer.speed_y *= -1
    elif len(computerPlayer_horizontal_wall_list) > 0:
        computerPlayer.speed_x *= -1
    #end if

    # move the computer player
    computerPlayer.move()

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