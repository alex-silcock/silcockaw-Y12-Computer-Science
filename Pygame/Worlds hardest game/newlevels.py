import pygame
import json
import random

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

size = (1000,800)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("World's Hardest Game")

# -- Exit game flag set to false
game_over_level_1 = False
game_over_level_2 = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

def menu(screen):
    done = False
    font = pygame.font.Font('freesansbold.ttf', 70)
    CentreX = size[0] // 2
    CentreY = size[1] // 2
    textcolour = BLUE
    while not done:
        screen.fill(WHITE)
        mouse = pygame.mouse.get_pos()
        text = font.render("PLAY", 5, textcolour)
        textRect = text.get_rect()
        textRect.center = (CentreX, CentreY)
        screen.blit(text, textRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return 'done'
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    done = True
                    return 'done'
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if textRect.collidepoint(mouse):
                    textcolour = RED
                    return 'play'
                #end if
            #end if
        #next event
        clock.tick(60)
    #end while    
#end function

font = pygame.font.SysFont("freesansbold.ttf", 30)
def print_text(x_pos, y_pos, screen, text_string, colour):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, colour)
    screen.blit(text_map, [x_pos, y_pos])


level_list = ["Pygame/Worlds hardest game/level1.JSON", "Pygame/Worlds hardest game/level2.JSON"]

class Game(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level

        if self.level == 1:
            self.ball_group = pygame.sprite.Group()
            self.all_sprites_group = pygame.sprite.Group()
            self.wall_list = pygame.sprite.Group()
            self.player_group = pygame.sprite.Group()
            self.startzone_group = pygame.sprite.Group()
            self.endzone_group = pygame.sprite.Group()

            file = open(level_list[level - 1], "r")
            theMazeArray = json.load(file)
            file.close() 
        
            self.ball1 = Ball(450, 150, 8, 50, 50)
            self.ball_group.add(self.ball1)
            self.all_sprites_group.add(self.ball1)

            self.ball2 = Ball(450, 250, -8, 50, 50)
            self.ball_group.add(self.ball2)
            self.all_sprites_group.add(self.ball2)

            self.ball3 = Ball(450, 350, 8, 50, 50)
            self.ball_group.add(self.ball3)
            self.all_sprites_group.add(self.ball3)

            self.ball4 = Ball(450, 430, -8, 50, 50)
            self.ball_group.add(self.ball4)
            self.all_sprites_group.add(self.ball4)

            self.startzone = StartZone(15, 210, 150, 180)
            self.startzone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            self.endzone = EndZone(840, 200, 150, 180)
            self.endzone_group.add(self.endzone)
            self.all_sprites_group.add(self.endzone)

            self.player = Player(80,250, 40, 40)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)
            self.attempts = 0

            

            for i in range (len(theMazeArray)):
                for j in range (len(theMazeArray[i])):
                    if theMazeArray[i][j] == 1:
                        self.newwall = Wall(j*10,i*10)
                        self.wall_list.add(self.newwall)
                        self.all_sprites_group.add(self.newwall)

        elif self.level == 2:
            self.ball_group = pygame.sprite.Group()
            self.all_sprites_group = pygame.sprite.Group()
            self.wall_list = pygame.sprite.Group()
            self.player_group = pygame.sprite.Group()
            self.startzone_group = pygame.sprite.Group()
            self.endzone_group = pygame.sprite.Group()

            file = open(level_list[level - 1], "r")
            theMazeArray = json.load(file)
            file.close() 
            
            self.ball1 = Ball(60, 150, 8, 20, 20)
            self.ball_group.add(self.ball1)
            self.all_sprites_group.add(self.ball1)

            self.ball2 = Ball(60, 190, -8, 20, 20)
            self.ball_group.add(self.ball2)
            self.all_sprites_group.add(self.ball2)

            self.ball3 = Ball(60, 230, 8, 20, 20)
            self.ball_group.add(self.ball3)
            self.all_sprites_group.add(self.ball3)

            self.ball4 = Ball(60, 270, -8, 20, 20)
            self.ball_group.add(self.ball4)
            self.all_sprites_group.add(self.ball4)

            

            self.startzone = StartZone(35, 60, 65, 80)
            self.startzone_group.add(self.startzone)
            self.all_sprites_group.add(self.startzone)

            self.endzone = EndZone(390, 60, 70, 90)
            self.endzone_group.add(self.endzone)
            self.all_sprites_group.add(self.endzone)

            self.player = Player(50, 80, 15, 15)
            self.player_group.add(self.player)
            self.all_sprites_group.add(self.player)
            self.attempts = 0

            

            for i in range (len(theMazeArray)):
                for j in range (len(theMazeArray[i])):
                    if theMazeArray[i][j] == 1:
                        self.newwall = Wall(j*10,i*10)
                        self.wall_list.add(self.newwall)
                        self.all_sprites_group.add(self.newwall)



    def update(self):
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        #player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()

        if self.level == 1:
            print_text(30, 30, screen, "Attempts: {}".format(self.attempts), RED)
            #ball collisions with wall
            self.ball_hit_wall_list = pygame.sprite.groupcollide(self.ball_group, self.wall_list, False, False)
            for b in self.ball_hit_wall_list:
                b.change_direction()
                
            #player collisions with ball
            self.player_hit_ball_list = pygame.sprite.groupcollide(self.ball_group, self.player_group, False, True)
            if len(self.player_hit_ball_list) > 0:
                self.player = Player(80, 250, 40, 40)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                self.attempts += 1  

            #player collisions with wall                   
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_list, False)
            if len(self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y

            #boundaries for end zone
            self.player_in_endzone = pygame.sprite.spritecollide(self.player, self.endzone_group, False)
            if len(self.player_in_endzone) > 0:
                return True
            else: return False

        elif self.level == 2:
            print_text(30, 30, screen, "Attempts: {}".format(self.attempts), RED)
            #ball collisions with wall
            self.ball_hit_wall_list = pygame.sprite.groupcollide(self.ball_group, self.wall_list, False, False)
            for b in self.ball_hit_wall_list:
                b.change_direction()
                
            #player collisions with ball
            self.player_hit_ball_list = pygame.sprite.groupcollide(self.ball_group, self.player_group, False, True)
            if len(self.player_hit_ball_list) > 0:
                self.player = Player(50, 80, 15, 15)
                self.player_group.add(self.player)
                self.all_sprites_group.add(self.player)
                self.attempts += 1  

            #player collisions with wall                   
            self.player_hit_wall_list = pygame.sprite.spritecollide(self.player, self.wall_list, False)
            if len(self.player_hit_wall_list) > 0:
                self.player.set_speed(0, 0)
                self.player.rect.x = self.player_old_x
                self.player.rect.y = self.player_old_y
            
            self.player_old_x = self.player.rect.x
            self.player_old_y = self.player.rect.y

            #boundaries for end zone
            self.player_in_endzone = pygame.sprite.spritecollide(self.player, self.endzone_group, False)
            if len(self.player_in_endzone) > 0:
                return True
            else: return False

        



class Wall(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        width = 10
        height = 10
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

        

class Ball(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, x_speed, width, height):
        super().__init__()
        self.change_x = x_speed
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

    def update(self):
        self.rect.x += self.change_x

    def change_direction(self):
        self.change_x *= -1


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

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
 
    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def set_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.x += y_val
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

# else statement skips straight to level 2
start_menu = menu(screen)
if start_menu == 'play': game_over_level_1 = False
else: game_over_level_1 = True


game = Game(1)
while not game_over_level_1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_level_1 = True
            pygame.quit()
    
    screen.fill(WHITE)
    game_over_level_1 = game.update()
    pygame.display.flip()
    clock.tick(60)
game = Game(2)
while not game_over_level_2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_level_2 = True
    
    screen.fill(WHITE)
    game.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
