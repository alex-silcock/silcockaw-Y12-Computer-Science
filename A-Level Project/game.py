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
PURPLE = (153,50,204)
coloursList = [BLACK, WHITE, BLUE, YELLOW, RED, LIGHTGREEN, LIGHTBLUE, PURPLE]

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
screen_width = 1300
screen_height = 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

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

#creating a timestamp of when the game was first run
totaltime = time.time()
#declare the number of attempts the user has taken
user_attempts = 0

poweruptimestart = time.time()
powerupactive = False
#Game class, houses everything thats instantiatiated and updated within the game
class Game(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        #anything that is used for all levels goes here
        #takes level as an argument and assigns it to the attribute
        self.level = level
        #create all sprite groups that need to be used in the game
        self.enemy_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.startZone_group = pygame.sprite.Group()
        self.endZone_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.laser_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.inputbox_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()

        #declare the starting score
        self.score = 0        

        #instantiating classes for level 0, which is the first level of the game
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

            #instantiate the player in the start zone, add to necessary groups
            self.player = Player(100, 380, 25, 25)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)


        #instantiating classes for level 1, which is the second level of the game
        elif self.level == 1:
            #opens the map from the level list, loads it, then closes it
            file = open(level_list[self.level], "r")
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

            #instantiate the start zone, add to necessary groups
            self.startzone = StartZone(70, 50, 150, 180)
            self.startZone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            #instantiate the player in the start zone, add to necessary groups
            self.player = Player(125, 115, 25, 25)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)

            #instantiate a ball which moves around in a circle, add to necessary groups
            self.ball = Ball(WHITE, 10, 100, 100, 360, 610, 100, 0.08)
            self.ball_group.add(self.ball)
            self.all_sprites_group.add(self.ball)

            #instantiate the enemy and add to necessary groups
            self.enemy = Enemy(830, 700, 0, 4, 30, 30)
            self.enemy_group.add(self.enemy)
            self.all_sprites_group.add(self.enemy)

            #instantiate the laser and add to necessary groups
            self.laser = Laser(555, 160, 3, 130)
            self.laser_group.add(self.laser)
            self.all_sprites_group.add(self.laser)

            #instantiate the enemy that moves around in a circle, and add to necessary groups
            self.ball = Ball(WHITE, 10, 900, 700, 830, 635, 70, 0.06)
            self.ball_group.add(self.ball)
            self.all_sprites_group.add(self.ball)

            #instantiate the different coins in different positions and add to necessary groups
            self.coin = Coin(100, 720)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            self.coin = Coin(370, 200)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            self.coin = Coin(650, 720)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            self.powerup = Powerup(150, 350)
            self.powerup_group.add(self.powerup)
            self.all_sprites_group.add(self.powerup)

        #instantiating classes for level 2, which is the third level of the game
        elif self.level == 2:
            #open map for level
            file = open(level_list[self.level], "r")
            mazeArray = json.load(file)
            file.close()

            #declare the number of keys the user has picked up
            self.keys = 0
            #declare the state of the door
            self.door_locked = True
            

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
            self.player = Player(0, 115, 25, 25)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)

            #instantiate the lasers in their positions and add to necessary groups
            self.laser1 = Laser(350, 560, 3, 200)
            self.laser_group.add(self.laser1)
            self.all_sprites_group.add(self.laser1)
            
            self.laser2 = Laser(450, 560, 3, 200)
            self.laser_group.add(self.laser2)
            self.all_sprites_group.add(self.laser2)

            self.laser3 = Laser(550, 560, 3, 200)
            self.laser_group.add(self.laser3)
            self.all_sprites_group.add(self.laser3)

            #instantiate the enemy that moves around a circle and add to necessary groups
            self.ball = Ball(WHITE, 10, 900, 700, 710, 220, 130, 0.1)
            self.ball_group.add(self.ball)
            self.all_sprites_group.add(self.ball)

            #instantiate the door which the user needs to key to get through, and add to necessary groups 
            self.door = Door(620, 450, 260, 5, PURPLE)
            self.door_group.add(self.door)
            self.all_sprites_group.add(self.door)

            #instantiate the key and add to necessary groups
            self.key = Key(320, 420)
            self.key_group.add(self.key)
            self.all_sprites_group.add(self.key)

            #instantiate the different coins in place for the level, add to necessary groups
            self.coin = Coin(120, 430)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            self.coin = Coin(830, 720)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            self.coin = Coin(510, 320)
            self.coin_group.add(self.coin)
            self.all_sprites_group.add(self.coin)

            #instantiate the end zone, add to end zone group and all sprites group
            self.endzone = EndZone(1110, 400, 180, 120)
            self.endZone_group.add(self.endzone)
            self.all_sprites_group.add(self.endzone)
        #end if
    #end procedure

    def update(self):
        #update + draw all_sprites_group
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        #handles player movement with the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()
        
        #handles bullets for when the user presses the space bar
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (self.player.bullet_count > 0):
                    self.bullet = Bullet(2, 0, self.player.rect.x, self.player.rect.y) 
                    self.bullet_group.add(self.bullet)
                    #self.player.decrease_bullets()
                    self.all_sprites_group.add(self.bullet)


        #creates the timer on the screen, uses the global var totaltime as the reference timestamp
        self.time = time.time()
        timer = round(abs(self.time - totaltime),1)
        #displays the timer on the screen for the user to see
        print_text(600, 10, screen, "Timer: {}".format(timer), RED)

        #updates needed for the first level
        if self.level == 0:

            #collisions for player with walls
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_group, False)
            #checks if player collided with wall, if they have then set their speed to 0
            if len(self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            #end if
            
            #necessary for player collisions with the wall
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y
            
            #collisions for player with end zone, if they collide with endzone, move onto next level
            global user_name
            self.player_hit_endZone_list = pygame.sprite.spritecollide(self.player, self.endZone_group, False)
            if len(self.player_hit_endZone_list) > 0:

                f = open("A-Level Project/leaderboard.txt", "a")
                f.write('\n' "Name: " + user_name + ", time: " + str(timer) + " seconds" + ", score: " + str(self.score))
                f.close()
                return True 
   
        #updates needed for the second level
        elif self.level == 1:
            
            #collisions for player with walls
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_group, False)
            #checks if player collided with wall, if they have then set their speed to 0
            if len (self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            #end if

            #necessary for player collisions with the wall
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y
            
            #boundaries for end zone, if the player completes the second level, move them onto the third level
            if (self.player.rect.y >= 60 and self.player.rect.y <= 175) and self.player.rect.x > 1300:
                return True

            #player collisions with the moving circles
            self.player_hit_moving_circles = pygame.sprite.groupcollide(self.player_group, self.ball_group, True, False)
            #checks if the player collides with the enemy, if they have reinstantiate the player in the start zone
            #add 1 to their total attempts
            global user_attempts
            if len (self.player_hit_moving_circles) > 0:
                self.player = Player(125, 115, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                user_attempts += 1


            #if enemy collides with the wall and it's only moving on the y plane, then only change it's y direction
            self.enemy_collide_wall_y = pygame.sprite.spritecollide(self.enemy, self.wall_group, False)
            if len(self.enemy_collide_wall_y) > 0:
                self.enemy.change_y_direction()

            #player colliding with enemy that just moves up and down
            self.enemy_collide_player = pygame.sprite.groupcollide(self.player_group, self.enemy_group, True, False)
            #checks if the player collides with the enemy, if they have reinstantiate the player in the start zone
            #add 1 to their total attempts
            if len(self.enemy_collide_player) > 0:
                self.player = Player(125, 115, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                user_attempts += 1

            #create new timestamp, used to know when to turn the laser on and off
            self.t1 = time.time()

            #find the difference in the timestamps which will give the timer
            dt = self.t1 - self.laser.time_of_creation

            
            #if the difference (time ran for) is greater than 3 then remove the laser
            #after another 0.6 seconds, turn the laser back on
            if dt > 3:
                self.laser.remove()

            #turning the laser back on by reinstantiating the laser
            if dt > 3.6:
                self.laser = Laser(555,160, 3, 130)
                self.laser_group.add(self.laser)
                self.all_sprites_group.add(self.laser)
                self.laser.time_of_creation = self.t1

            #checks for player collisions with the laser, if they collide, then reinstantiate the player
            #add 1 to the players total attempts
            self.player_collide_with_laser = pygame.sprite.groupcollide(self.player_group, self.laser_group, True, False)
            if len(self.player_collide_with_laser) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                user_attempts += 1

            self.player_collide_with_coin = pygame.sprite.groupcollide(self.player_group, self.coin_group, False, True)
            if len(self.player_collide_with_coin) > 0:
                #add one to the score
                self.score += 1

            
            #player colliding with powerup
            global poweruptimestart, powerupactive
            self.player_collide_with_powerup = pygame.sprite.groupcollide(self.player_group, self.powerup_group, False, True)
            if len(self.player_collide_with_powerup) > 0 and powerupactive == False:
                poweruptimestart = time.time()
                powerupactive = True
                powerupvalue = self.powerup.call_powerup()

                #if the powerup value is 0, then enlarge the player
                if powerupvalue == 0:
                    playerx = self.player.rect.x
                    playery = self.player.rect.y
                    self.player.kill()
                    self.player = Player(playerx, playery, 40, 40)
                    self.player_group.add(self.player)
                    self.all_sprites_group.add(self.player)

                #if the powerup value is 1, then speedup the player
                elif powerupvalue == 1:
                    self.player.speedup()

                #if the powerup value is 2, then enlarge the player
                elif powerupvalue == 2:
                    self.player.slowdown()
                #end if

            currentpoweruptime = time.time()
            timerunningpowerup = abs(currentpoweruptime - poweruptimestart)

            if timerunningpowerup > 3:
                playerx = self.player.rect.x
                playery = self.player.rect.y
                self.player.kill()
                self.player = Player(playerx, playery, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player) 
                self.player.change_speed(5) 
                powerupactive = False    


            #drawing the number of attempts on the screen
            print_text(10, 10, screen, "Attempts: {}".format(user_attempts), RED)
            #drawing the score on the screen
            print_text(300, 10, screen, "Score: {}".format(self.score), RED)



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

            self.player_hit_endZone_list = pygame.sprite.spritecollide(self.player, self.endZone_group, False)
            if len(self.player_hit_endZone_list) > 0:
                return True

            #create new timers for each laser 
            self.t1 = time.time()
            self.t2 = time.time()
            self.t3 = time.time()

            #find the difference in the times for each laser
            dt1 = self.laser1.time_of_creation - self.t1
            dt2 = self.laser2.time_of_creation - self.t2
            dt3 = self.laser3.time_of_creation - self.t3

            #ithis controls when the lasers turn on and off
            if abs(dt1) > 3:
                self.laser1.remove()

            if abs(dt1) > 3.6:
                self.laser1 = Laser(350, 560, 3, 200)
                self.laser_group.add(self.laser1)
                self.all_sprites_group.add(self.laser1)
                self.laser1.time_of_creation = self.t1

            if abs(dt2) > 3.2:
                self.laser2.remove()

            if abs(dt2) > 3.8:
                self.laser2 = Laser(450, 560, 3, 200)
                self.laser_group.add(self.laser2)
                self.all_sprites_group.add(self.laser2)
                self.laser2.time_of_creation = self.t2

            if abs(dt3) > 3.4:
                self.laser3.remove()

            if abs(dt3) > 4:
                self.laser3 = Laser(550, 560, 3, 200)
                self.laser_group.add(self.laser3)
                self.all_sprites_group.add(self.laser3)
                self.laser3.time_of_creation = self.t3

            self.player_collide_key = pygame.sprite.spritecollide(self.player, self.key_group, True)
            if len(self.player_collide_key) > 0:
                self.keys += 1
                self.door_locked = False

            #player collisions with the laser
            self.player_collide_with_laser = pygame.sprite.groupcollide(self.player_group, self.laser_group, True, False)
            if len(self.player_collide_with_laser) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                user_attempts += 1

            #player collisions with the door
            self.player_collide_door = pygame.sprite.spritecollide(self.player, self.door_group, False)
            if self.door_locked == True and len(self.player_collide_door) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x1
                self.player.rect.y = self.player_old_y1
            
            elif self.door_locked == False and len(self.player_collide_door) > 0:
                self.door.open_door()

            #end if
            
            #necessary for collisions
            self.player_old_x1 = self.player.rect.x
            self.player_old_y1 = self.player.rect.y

            self.player_hit_moving_circles = pygame.sprite.groupcollide(self.player_group, self.ball_group, True, False)
            if len (self.player_hit_moving_circles) > 0:
                #reinstantiate the player in the start zone
                self.player = Player(125, 115, 25, 25)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                user_attempts += 1

            self.player_collide_with_coin = pygame.sprite.groupcollide(self.player_group, self.coin_group, False, True)
            if len(self.player_collide_with_coin) > 0:
                #add one to the score
                self.score += 1

            #drawing the number of attempts on the screen
            print_text(10, 10, screen, "Attempts: {}".format(user_attempts), RED)
            #drawing the score on the screen
            print_text(300, 10, screen, "Score: {}".format(self.score), RED)

    #end procedure
#end class

#define Player class with necessary attributes and methods 
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
    
    def speedup(self):
        self.speed = 7
    #end procedure

    def slowdown(self):
        self.speed = 3
    #end procedure

    def change_speed(self, speed):
        self.speed = speed
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
    def __init__(self, x1, y1, width, height):

        super().__init__()
        
        self.width = width
        self.height = height
        self.color = RED
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.time_of_creation = time.time()

    def remove(self):
        self.kill()

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()

        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def open_door(self):
        self.kill()

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("A-Level Project/Files/key2.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 15
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def call_powerup(self):
        self.chosenpowerup = (random.randrange(0, 2))
        #powerup 0 will enlarge the player
        if self.chosenpowerup == 0:
            return 0
        #powerup 1 will speed up the player
        elif self.chosenpowerup == 1:
            return 1
        #powerup 2 will slow down the player
        elif self.chosenpowerup == 2:
            return 2
        


#flag to determine whether key is being pressed
inp_keydown = False
#flag to check if name has been entered
nameEntered = False
#user's name they input
user_name = ''
class InputBox:
    # text box to enter name
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False


    def handle_event(self, event):
        
        global inp_keydown
        global user_name
        global nameEntered
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos) and nameEntered == False:
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN and inp_keydown == False:
            inp_keydown = True
            if self.active:
                if event.key == pygame.K_RETURN and nameEntered == False:
                    user_name = self.text
                    self.text = ''
                    nameEntered = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    
                if nameEntered == True:
                    self.active = False
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

        elif event.type == pygame.KEYUP:
            inp_keydown = False

        #if the user doesn't enter a name, theyre assigned a random username
        if user_name == '':
            user_name = ("user" + str(random.randrange(1, 100000000)))

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def menu(screen):
    finished = False
    textcolour = WHITE
    textcolour_2 = WHITE
    textcolour_3 = WHITE
    
    
    inputbox = InputBox(500, 150, 30, 30)

    while finished == False:
        for event in pygame.event.get():
            inputbox.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if textRect.collidepoint(mouse):
                    leaderboard_screen(screen)




        # Background Image
        screen.fill(BLACK)


        inputbox.update()
        inputbox.draw(screen)



        mouse = pygame.mouse.get_pos()

        global nameEntered

        if nameEntered == True:
            print_text(510, 160, screen, "NAME ENTERED", RED)

        
        print_text(500, 110, screen, "ENTER NAME BELOW", WHITE)
        print_text(500, 300, screen, "USE THE ARROW KEYS TO MOVE", WHITE)
        print_text(500, 300 + 30, screen, "PRESS SPACE TO SHOOT BULLETS", WHITE)
        print_text(500, 300 + 60, screen, "AVOID THE ENEMIES", WHITE)
        print_text(500, 300 + 90, screen, "USE THE ARROW KEYS TO MOVE", WHITE)
        print_text(500, 300 + 120, screen, "COLLECT THE COINS FOR EXTRA POINTS", WHITE)
        print_text(500, 300 + 150, screen, "PRESS RIGHT SHIFT TO START", WHITE)

        text = font.render("LEADERBOARD", 5, textcolour)
        textRect = text.get_rect()
        textRect.center = (577, 600)
        screen.blit(text, textRect)

        if textRect.collidepoint(mouse):
            textcolour = RED
        else:
            textcolour = WHITE

        

        #reset the timer
        global totaltime
        totaltime = time.time()

        pygame.display.flip()
        clock.tick(60)

instructions = [line.strip('\n') for line in open("A-Level Project/leaderboard.txt", "r").readlines()]

def draw_txt_file():
    for n, line in enumerate(instructions):
        text = font.render(line, 1, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen_width//2
        text_rect.centery = n*25 + 50
        screen.blit(text, text_rect)

def leaderboard_screen(screen):
    finished = False
    textcolour = WHITE
      

    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                #if b key is pressed go back to the menu
                if event.key == pygame.K_b:
                    #menu(screen)
                    finished = True
        
        draw_txt_file()
        # Background Image
        screen.fill(BLACK)
                
        print_text(30, 30, screen, "PRESS B TO GO BACK", WHITE)

        mouse = pygame.mouse.get_pos()

        pygame.display.flip()
        clock.tick(60)

def end_game(screen):
    finished = False
    textcolour = WHITE
    textcolour_2 = WHITE

    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if textRect.collidepoint(mouse):
                    menu(screen)
                if textRect_2.collidepoint(mouse):
                    leaderboard_screen(screen)

        
        # Background Image
        screen.fill(BLACK)
                
        print_text(500, 150, screen, "CONGRATULATIONS", WHITE)

        mouse = pygame.mouse.get_pos()

        text = font.render("MENU", 5, textcolour)
        textRect = text.get_rect()
        textRect.center = (600, 300)
        screen.blit(text, textRect)

        text_2 = font.render("LEADERBOARD", 5, textcolour_2)
        textRect_2 = text_2.get_rect()
        textRect_2.center = (600, 350)
        screen.blit(text_2, textRect_2)

        if textRect.collidepoint(mouse):
            textcolour = RED
        else:
            textcolour = WHITE

        if textRect_2.collidepoint(mouse):
            textcolour_2 = RED
        else:
            textcolour_2 = WHITE

        pygame.display.flip()
        clock.tick(60)






menu(screen)
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
            level2Finished = True
            pygame.quit()

    screen.fill(BLACK)

    #game updates inside the loop 
    level1Finished = game.update()
    pygame.display.flip()
    clock.tick(60) 
#end while

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

end_game(screen)
pygame.quit()
