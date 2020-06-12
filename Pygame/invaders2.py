import pygame
import random
import math
#import os
#print (os.getcwd())

# -- Global Constants

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

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
def print_text(x_pos, y_pos, screen, text_string, colour):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, colour)
    screen.blit(text_map, [x_pos, y_pos])
#end procedure

## -- Define the class Invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height, speed, enemy_image):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.image.load(enemy_image)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = speed
    #End Procedure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= size[1]:
            self.rect.y = 0
            self.image = pygame.image.load("Pygame/Files/invader.jpg")
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
        self.score = 0
        self.bullet_count = 50
    #end func

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

    def increase_score(self, val):
        self.score += val
    #end procedure

    def decrease_bullets(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
        #end if
    #end procedure

    def decrease_lives(self, val):
        self.lives -= val
    #end procedure
#end class

class Bullet(pygame.sprite.Sprite):
    # Define the constructor for Bullet
    def __init__(self, color, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([5,5])
        self.image.fill(RED)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = my_player.rect.x
        self.rect.y = my_player.rect.y
        self.speed = speed
    #end procedure

    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #end procedure
#end class


# Create a list of all different sprite groups
invader_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the invaders
number_of_invaders = 30
invader_width = 20
invader_height = 20

for x in range(number_of_invaders):
    invader_speed = random.randrange(1,2)
    my_invader = Invader(BLUE, invader_width, invader_height, invader_speed, "Pygame/Files/silcock.jpg")
    invader_group.add(my_invader)
    all_sprites_group.add(my_invader) # adds it to the group of all Sprites
#Next x



# Creating the player
player_width = 10
player_height = 10
my_player = Player(YELLOW, player_width, player_height, 0, 5)
player_group.add(my_player)
all_sprites_group.add(my_player)

# ======= game loop ======= #
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True      
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP  and my_player.bullet_count > 0:
                bullet = Bullet(RED, -2)
                bullet_group.add(bullet)
                my_player.decrease_bullets()
                all_sprites_group.add(bullet)
                #pygame.mixer.music.load('shooting.mp3')
                #pygame.mixer.music.play(0)
            #end if
        #end if
    #next event

    # mechanics for each bullet
    for bullet_shot in bullet_group:
        invader_hit_group = pygame.sprite.spritecollide(bullet_shot, invader_group, True)

        # for each block hit, remove the bullet and add to the score
        for bullet_shot in invader_hit_group:
            my_player.increase_score(5)
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)
        #next bullet_shot
        # remove the bullet if it flies up off the screen
        if bullet.rect.y < 0:
            bullet_group.remove(bullet)
            all_sprites_group.remove(bullet)
        #end if
    #next bullet_shot

    # moving the player on key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_player.player_set_speed(-3)
    elif keys[pygame.K_RIGHT]:
        my_player.player_set_speed(3)
    #end if
    
    
    # -- User inputs here
    
    
    # -- Game logic goes after this comment
    all_sprites_group.update()

    # when invader hits the player add 5 to the score
    player_hit_group = pygame.sprite.spritecollide(my_player, invader_group, True) 
    for p in player_hit_group:
        my_player.decrease_lives(1)
    #next p
    if my_player.lives == 0 or my_player.bullet_count < 0:
        done = True
    #end if

    
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    all_sprites_group.draw(screen)
    

    print_text(20, 50, screen, "Lives : %d" % my_player.lives, WHITE)
    print_text(20, 80, screen, "Score : %d" % my_player.score, WHITE)
    print_text(20, 110, screen, "Bullets : %d" % my_player.bullet_count, WHITE)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop

pygame.quit()