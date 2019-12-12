import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

size = (1000,800)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Game Class Testing")

# -- Exit game flag set to false
game_over = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ball_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        
        self.ball = Ball(100,100,BLUE)
        self.all_sprites_group.add(self.ball)
        self.ball_group.add(self.ball)

        self.player = Player(150,150, 3)
        self.all_sprites_group.add(self.player)
        self.player_group.add(self.player)     
    
    def update(self):
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        self.player_hit_ball_list = pygame.sprite.spritecollide(self.player, self.ball_group, True)
        

        

class Ball(pygame.sprite.Sprite):
    def __init__(self, x_co, y_co, colour):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_co
        self.rect.y = y_co

    def update(self):
        self.rect.x += 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x_co, y_co, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface([50,50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_co
        self.rect.y = y_co
        

        

    def move_up(self):
        self.rect.y -= self.speed
    #end proc
    def move_down(self):
        self.rect.y += self.speed
    #end proc
    def move_right(self):
        self.rect.x += self.speed
    #end proc
    def move_left(self):
        self.rect.x -= self.speed
    #end proc

game = Game()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True      
        #end if
    #next event
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        game.player.move_up()
    elif keys[pygame.K_DOWN]:
        game.player.move_down()
    elif keys[pygame.K_RIGHT]:
        game.player.move_right()
    elif keys[pygame.K_LEFT]:
        game.player.move_left()

    
    screen.fill(WHITE)
    
    game.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
