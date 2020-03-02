# zen mode = CTRL + K then press Z
# don't forget to put end tags for everything e.g. end if
# use meaningful variable names
# don't forget to add comments for what i am doing
# have a starting level where the user just goes straight from
# one part to the other and gives them the rules etc. as they go over certain parts


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
pygame.display.set_caption("Maze Kingdom")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

# creating a function that draws text on the screen in the x_pos and y_pos taken as arguments
font = pygame.font.SysFont("freesansbold.ttf", 30)
def print_text(x_pos, y_pos, screen, text_string, colour):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, colour)
    screen.blit(text_map, [x_pos, y_pos])
#end procedure

#creating a list of all the levels
level_list = ["A-Level Project/level1.JSON"]

class Game(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        # anything that is used for all levels goes here
        self.level = level
        self.box_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.startZone_group = pygame.sprite.Group()
        self.endZone_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()

        if self.level == 1:
            #opens the map from the level list, loads it, then closes it
            file = open(level_list[level - 1], "r")
            mazeArray = json.load(file)
            file.close()

            #instantiate the walls
            for i in range (len(mazeArray)):
                for j in range (len(mazeArray[i])):
                    if mazeArray[i][j] == 1:
                        self.newwall = Wall(j*10,i*10)
                        self.wall_group.add(self.newwall)
                        self.all_sprites_group.add(self.newwall)
                    #end if
                #next j
            #next i

            #instantiate the start zone
            self.startzone = StartZone(70, 50, 150, 180)
            self.startZone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            #instantiate tha player in the start zone
            self.player = Player(125, 115)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)
        #end if
    #end procedure

    def update(self):
        #update + draw all_sprites_group
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        #player movement, data hiding, only allows the attributes to be changed through a function
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()
        #end if

        if self.level == 1:
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_group, False)
            if len (self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            #end if
        #necessary for collisions
        self.player_old_x = self.player.rect.x
        self.player_old_y = self.player.rect.y

        #boundaries for end zone
        if (self.player.rect.y >= 60 and self.player.rect.y <= 175) and self.player.rect.x > 1300:
            return True
        #end if
    #end procedure
#end class

class Player(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.width = 25
        self.height = 25
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.speed = 5
    #end procedure
    
    # class methods

    def move_up(self):
        self.rect.y -= self.speed
    #end procedure

    def move_down(self):
        self.rect.y += self.speed
    #end procedure
 
    def move_right(self):
        self.rect.x += self.speed
    #end procedure

    def move_left(self):
        self.rect.x -= self.speed
    #end procedure

    def set_speed(self, x_speed, y_speed):
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
    #end procedure

    # class methods
    def draw(self):
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)
    #end procedure
#end class

class Wall(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        width = 10
        height = 10
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure
#end class

class StartZone(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure
#end class

class EndZone(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(LIGHTGREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure
#end class

#instantiate the game class for the first level 
game = Game(1)
while not level1Finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level1Finished = True
            pygame.quit()

    screen.fill(BLACK)

    #game updates inside the loop 
    level1Finished = game.update()
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()
#instantiate the game class for the second level

#instantiate the game class for the third level






    