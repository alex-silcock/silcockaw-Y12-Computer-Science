import pygame
import json

# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)
RED = (255,0,0)

game_over = False

pygame.init()

size = (500,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Djikstras Algorithm")

clock = pygame.time.Clock()

file = open("Pygame/Shortest paths/map.JSON","r")
theMazeArray = json.load(file)
file.close()

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wall_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.player = Player(30,30,8,8)
        self.player_group.add(self.player)
        self.all_sprites_group.add(self.player)
        
        for i in range (len(theMazeArray)):
            for j in range (len(theMazeArray[i])):
                if theMazeArray[i][j] == 1:
                    self.newwall = Wall(j*10,i*10)
                    self.wall_group.add(self.newwall)
                    self.all_sprites_group.add(self.newwall)
                #end if
            #next j
        #next i
    #end procedure
    
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
        #end if

        self.player_hit_wall_group = pygame.sprite.spritecollide(self.player, self.wall_group, False)
        if len(self.player_hit_wall_group) > 0:
            self.player.set_speed(0, 0)
            self.player.rect.x = self.player_old_x
            self.player.rect.y = self.player_old_y
        #end if

        self.player_old_x = self.player.rect.x
        self.player_old_y = self.player.rect.y
    #end procedure
#end class


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
        self.speed = 2
    #end procedure

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

    def set_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.x += y_val
    #end procedure
#end class

            
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        width = 10
        height = 10
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    #end procedure
#end class

game = Game()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True      
        #end if
    #next event
    
    screen.fill(BLACK)
    
    game.update()

    pygame.display.flip()
    clock.tick(60)
#end while
pygame.quit()

