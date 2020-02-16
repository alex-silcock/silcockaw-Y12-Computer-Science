# zen mode = CTRL + K then press Z


## program starts

# -- Library imports
import pygame, random, json

# -- Global constants
level1Finished = False
level2Finished = False
level3Finished = False


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

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Player(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.speed = 5
    #end procedure
    
    # class methods

    def player_move_up(self):
        self.rect.y -= self.speed
    #end procedure

    def player_move_down(self):
        self.rect.y += self.speed
    #end procedure
 
    def player_move_right(self):
        self.rect.x += self.speed
    #end procedure

    def player_move_left(self):
        self.rect.x -= self.speed
    #end procedure

    def player_set_speed(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed
    #end procedure
#end class
    
class Box(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, x_speed, y_speed, width, height):
        super().__init__()
        self.change_x = x_speed
        self.change_y = y_speed
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure

    # class methods

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
    #end procedure

    def change_x_direction(self):
        self.change_x *= -1
    #end procedure
    def change_y_direction(self):
        self.change_y *= -1
    #end procedure
#end class

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, radius, x_coord, y_coord):
        super().__init__()
        self.colour = colour
        self.radius = radius
        self.x = x_coord
        self.y = y_coord

    def draw_circle(self):
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)


while not level1Finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level1Finished = True
            pygame.quit()

    screen.fill(BLACK)
    # update the game here (game.update())

    pygame.display.flip()
    clock.tick(60) 
pygame.quit()






    