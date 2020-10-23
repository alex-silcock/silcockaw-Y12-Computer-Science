# zen mode = CTRL + K then press Z
# don't forget to put end tags for everything e.g. end if
# use meaningful variable names
# don't forget to add comments for what i am doing


## program starts

# -- Library imports
import pygame, random, json, math, time

# -- Global constants
level0Finished = False
level1Finished = False
level2Finished = False

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
level_list = ["A-Level Project/level0.JSON", "A-Level Project/level1.JSON", "A-Level Project/level2.JSON"]

class Game(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        # anything that is used for all levels goes here
        # create all sprite groups that need to be used in the game
        self.level = level
        self.enemy_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.startZone_group = pygame.sprite.Group()
        self.endZone_group = pygame.sprite.Group()
        self.informationBars_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.laser_group = pygame.sprite.RenderPlain()
        self.block_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()


        if self.level == 0:
            #opens the map from the level list, loads it, then closes it
            file = open(level_list[self.level], "r")
            mazeArray = json.load(file)
            file.close()

            #instantiate the walls
            #changes x and y coordinates accordingly
            for i in range (len(mazeArray)):
                for j in range (len(mazeArray[i])):
                    if mazeArray[i][j] == 1:
                        self.newwall = Wall(j*10,i*10)
                        self.wall_group.add(self.newwall)
                        self.all_sprites_group.add(self.newwall)
                    #end if
                #next j
            #next i

            #instantiate the start zone, add to start zone group and all sprites group
            self.startzone = StartZone(60, 310, 110, 170)
            self.startZone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            #instantiate the end zone, add to end zone group and all sprites group
            self.endzone = EndZone(1130, 310, 110, 170)
            self.endZone_group.add(self.endzone)
            self.all_sprites_group.add(self.endzone)

            #instantiate the information bars so when the player goes over them they get tips
            #new attribute 1 through 5 which determines the message displayed
            #move function print_text into class for each message
            self.informationbar = [InformationBars(300 + 180 * i, 310, 5, 170, i)for i in range(5)]
            self.informationBars_group.add(self.informationbar)
            self.all_sprites_group.add(self.informationbar)

            #instantiate the player in the start zone, add to necessary groups
            self.player = Player(100, 380)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)


        
        elif self.level == 1:
            #opens the map from the level list, loads it, then closes it
            file = open(level_list[self.level], "r")
            mazeArray = json.load(file)
            file.close()

            #declare the initial amount of attempts
            self.attempts = 0
            
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

            #instantiate the start zone, add to necessary groups
            self.startzone = StartZone(70, 50, 150, 180)
            self.startZone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            #instantiate the player in the start zone, add to necessary groups
            self.player = Player(125, 115)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)

            #instantiate a ball which moves around in a circle, add to necessary groups
            self.ball = Ball(WHITE, 10, 100, 100, 360, 610, 100, 0.08)
            self.ball_group.add(self.ball)
            self.all_sprites_group.add(self.ball)

            self.enemy = Enemy(830, 700, 0, 4, 30, 30)
            self.enemy_group.add(self.enemy)
            self.all_sprites_group.add(self.enemy)

            self.laser = Laser(555, 160)
            self.laser_group.add(self.laser)
            self.all_sprites_group.add(self.laser)

            self.ball = Ball(WHITE, 10, 900, 700, 830, 635, 70, 0.06)
            self.ball_group.add(self.ball)
            self.all_sprites_group.add(self.ball)

        elif self.level == 2:
            #open map for level
            file = open(level_list[self.level], "r")
            mazeArray = json.load(file)
            file.close()

            #declare variables for the level
            self.attempts = 0
            

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

            #instantiate the player in the start zone, add to necessary groups
            self.player = Player(0, 115)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)



        #end if
    #end procedure

    def update(self):
        #update + draw all_sprites_group
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        #player movement + events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and (self.player.bullet_count > 0):
                self.bullet = Bullet(2, 0, self.player.rect.x, self.player.rect.y) 
                self.bullet_group.add(self.bullet)
                #self.player.decrease_bullets()
                self.all_sprites_group.add(self.bullet)
            #end if
        #end if
        


        if self.level == 0:
            #collisions for player with walls
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_group, False)
            if len(self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            #end if
            

            #necessary for collisions
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y
            
            #collisions for player with end zone
            self.player_hit_endZone_list = pygame.sprite.spritecollide(self.player, self.endZone_group, False)
            if len(self.player_hit_endZone_list) > 0:
                return True

            # trying to get the info bars on first level to change the text for each bar
            self.player_hit_informationbar_list = pygame.sprite.spritecollide(self.player, self.informationBars_group, False)
        
            '''messages:list = ["hello", "2"]
            messageno = 0
            if len(self.player_hit_informationbar_list) > 0:
                print_text(100,100,screen, messages[messageno], WHITE)    
                messageno =+ 1
            '''
    
        
        elif self.level == 1:

            #collisions for player with walls
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

            # player collisions with the moving circles
            self.player_hit_moving_circles = pygame.sprite.groupcollide(self.player_group, self.ball_group, True, False)
            if len (self.player_hit_moving_circles) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                self.attempts += 1


            # if enemy collides with the wall and it's only moving on the y plane
            self.enemy_collide_wall_y = pygame.sprite.spritecollide(self.enemy, self.wall_group, False)
            if len(self.enemy_collide_wall_y) > 0:
                self.enemy.change_y_direction()

            # player colliding with one plane enemy
            self.enemy_collide_player = pygame.sprite.groupcollide(self.player_group, self.enemy_group, True, False)
            if len(self.enemy_collide_player) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                self.attempts += 1

            #create new timer 
            self.t1 = time.time()

            #find the difference in the times
            dt = self.laser.time_of_creation - self.t1

            #if the difference (time ran for) is greater than 3 then remove the laser
            #after another 2 seconds, turn the laser back on
            if abs(dt) > 3:
                self.laser.remove()

            if abs(dt) > 3.6:
                self.laser = Laser(555,160)
                self.laser_group.add(self.laser)
                self.all_sprites_group.add(self.laser)
                self.laser.time_of_creation = self.t1

            self.player_collide_with_laser = pygame.sprite.groupcollide(self.player_group, self.laser_group, True, False)
            if len(self.player_collide_with_laser) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                self.attempts += 1


            #drawing the number of attempts on the screen
            print_text(10, 10, screen, "Attempts: {}".format(self.attempts), RED)


        

        elif self.level == 2:
            #collisions for player with walls
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_group, False)
            if len (self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            #end if
            
            #necessary for collisions
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y

            #drawing the number of attempts on the screen
            print_text(10, 10, screen, "Attempts: {}".format(self.attempts), RED)
    #end procedure
#end class

#define Player class with necessary attributes and methods 
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
        self.bullet_count = 10
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

#define Enemy class with necessary attributes and methods 
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, x_speed, y_speed, width, height):
        super().__init__()
        self.change_x = x_speed
        self.change_y = y_speed
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
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

#define Ball class with necessary attributes and methods 
class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, radius, x_coord, y_coord, centre_x_orbit, centre_y_orbit, sizeOfOrbit, speed):
        super().__init__()
        self.colour = colour

        #the size of the ball
        self.radius = radius

        #the size of the orbit
        self.sizeOfOrbit = sizeOfOrbit

        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
        #the x and y coordinates of the ball
        self.rect.x = x_coord
        self.rect.y = y_coord

        #the "center" the sprite will orbit
        self.centre_x = centre_x_orbit
        self.centre_y = centre_y_orbit

        #current angle in radians
        self.angle = 0

        #how fast to orbit in radians per frame
        self.speed = speed

        pygame.draw.circle(self.image, self.colour, [self.radius, self.radius], self.radius)
    #end procedure

    #class methods
    def update(self):
        #Update the ball's position

        # Calculate a new x, y
        self.rect.x = self.sizeOfOrbit * math.sin(self.angle) + self.centre_x
        self.rect.y = self.sizeOfOrbit * math.cos(self.angle) + self.centre_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed
        
    #end procedure
#end class


#define Wall class with necessary attributes and methods 
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


#define StartZone class with necessary attributes and methods 
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

#define EndZone class with necessary attributes and methods 
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


#define InformationBars class with necessary attributes and methods 
class InformationBars(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, width, height, message):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.messages = ["Watch out for the enemies", "Collect the coins for points"]
    #end procedure

    def display_information(self, val):
        self.messages = ["Watch out for the enemies", "Collect the coins for points"]
        self.current_message = self.messages[val]
        print_text(100, 100, screen, self.current_message, WHITE)
    # end procedure
#end class

#define Bullet class with necessary attributes and methods 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_speed, y_speed, PlayerRectX, PlayerRectY):
        super().__init__()
        self.width = 5
        self.height = 5
        self.colour = RED
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = PlayerRectX
        self.rect.y = PlayerRectY

    #update function will move the bullet
    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed
    #end function 
#end class

class Laser(pygame.sprite.Sprite):
    def __init__(self, x1, y1):

        super().__init__()
        
        self.width = 3
        self.height = 130
        self.color = RED
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.time_of_creation = time.time()

    def remove(self):
        self.kill()




'''
#instantiate the game class for the starting level
game = Game(0)
#game loop for the starting / information level
while not level0Finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level0Finished = True
            pygame.quit()

    screen.fill(BLACK)
    
    #game updates inside the loop 
    level0Finished = game.update()
    pygame.display.flip()
    clock.tick(60) 
#end while


#instantiate the game class for the first level
game = Game(1)
#game loop for the first level
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
#end while
'''
#instantiate the game class for the second level
game = Game(2)
#game loop for the second level
while not level2Finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level2Finished = True
            pygame.quit()

    screen.fill(BLACK)

    #game updates inside the loop 
    level2Finished = game.update()
    pygame.display.flip()
    clock.tick(60) 
#end while
pygame.quit()

#instantiate the game class for the third level






    