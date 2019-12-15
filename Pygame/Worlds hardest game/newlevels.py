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
game_over = False

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
                    textcolour = WHITE
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


level_list = ["Pygame/Worlds hardest game/whg_map.JSON", "Pygame/Worlds hardest game/level2.JSON"]

class Game(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level

        self.ball_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        if self.level == 1:
            file = open(level_list[level - 1], "r")
            theMazeArray = json.load(file)
            file.close() 
        
            self.ball1 = Ball(450, 150, 8)
            self.ball_group.add(self.ball1)
            self.all_sprites_group.add(self.ball1)

            self.ball2 = Ball(450, 250, -8)
            self.ball_group.add(self.ball2)
            self.all_sprites_group.add(self.ball2)

            self.ball3 = Ball(450, 350, 8)
            self.ball_group.add(self.ball3)
            self.all_sprites_group.add(self.ball3)

            self.ball4 = Ball(450, 430, -8)
            self.ball_group.add(self.ball4)
            self.all_sprites_group.add(self.ball4)

            self.player = Player(80,250)
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
            file = open(level_list[level - 1], "r")
            theMazeArray = json.load(file)
            file.close() 
        
            self.ball_group = pygame.sprite.Group()
            self.all_sprites_group = pygame.sprite.Group()
            self.wall_list = pygame.sprite.Group()
            self.player_group = pygame.sprite.Group()
            
            self.ball1 = Ball(450, 150, 8)
            self.ball_group.add(self.ball1)
            self.all_sprites_group.add(self.ball1)

            self.ball2 = Ball(450, 250, -8)
            self.ball_group.add(self.ball2)
            self.all_sprites_group.add(self.ball2)

            self.ball3 = Ball(450, 350, 8)
            self.ball_group.add(self.ball3)
            self.all_sprites_group.add(self.ball3)

            self.ball4 = Ball(450, 430, -8)
            self.ball_group.add(self.ball4)
            self.all_sprites_group.add(self.ball4)

            self.player = Player(80,250)
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
        pygame.draw.rect(screen, LIGHTGREEN, (840, 200, 140, 170))
        pygame.draw.rect(screen, LIGHTBLUE, (15, 210, 145, 200))
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
            
        #ball collisions with wall
        self.ball_hit_wall_list = pygame.sprite.groupcollide(self.ball_group, self.wall_list, False, False)
        for b in self.ball_hit_wall_list:
            b.change_direction()
            
        #player collisions with ball
        self.player_hit_ball_list = pygame.sprite.groupcollide(self.ball_group, self.player_group, False, True)
        if len(self.player_hit_ball_list) > 0:
            self.player = Player(80, 250)
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
        if self.player.rect.x > 840 and self.player.rect.y > 200:
            self.level += 1

        print_text(30, 30, screen, "Attempts: {}".format(self.attempts), RED)

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
    def __init__(self, x_coord, y_coord, x_speed):
        super().__init__()
        self.change_x = x_speed
        self.image = pygame.Surface([50,50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord


    def update(self):
        self.rect.x += self.change_x


    def change_direction(self):
        self.change_x *= -1


class Player(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.image = pygame.Surface([40,40])
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



start_menu = menu(screen)
if start_menu == 'done':
    game_over = True
elif start_menu == 'play':
    game_over = False
#end if

level = 1
game = Game(level)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    screen.fill(WHITE)
    game.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()