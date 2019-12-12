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


file = open("Pygame/Worlds hardest game/whg_map.JSON", "r")
theMazeArray = json.load(file)
last_pressed = []
file.close()

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
        menu_ball_list = []
        for x in range(10):
            x_rand = random.randrange(size[0])
            y_rand = random.randrange(size[1])   
            colour_rand = random.choice(coloursList)
            rand_speed = random.randrange(15)
            ball = Ball(x_rand, y_rand, rand_speed)   
            menu_ball_list.append(ball)
        clock.tick(60)
    #end while    
#end function

class Wall(pygame.sprite.Sprite):
    # Define the constructor for the Walls
    def __init__(self, x_coord, y_coord):
        # Call the sprite constructor
        super().__init__()
        width = 10
        height = 10
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the attributes
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure
#end class

class Ball(pygame.sprite.Sprite):
    # Define the constructor for the Balls
    def __init__(self, x_coord, y_coord, x_speed):
        # Call the sprite constructor
        super().__init__()
        self.change_x = x_speed
        self.image = pygame.Surface([50,50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
    #end procedure

    def update(self):
        self.rect.x += self.change_x
    #end proc
#end class

class Player(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.speed = 5
    #end procedure

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
    def set_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.x += y_val
    #end proc
#end class

ball_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player_group = pygame.sprite.Group()

for i in range (len(theMazeArray)):
    for j in range (len(theMazeArray[i])):
        if theMazeArray[i][j] == 1:
            newwall = Wall(j*10,i*10)
            wall_list.add(newwall)
            all_sprites_group.add(newwall)
        #end if
    #next j
#next i 

# Instantiating each sprite
ball1 = Ball(450, 150, 8)
ball_group.add(ball1)
all_sprites_group.add(ball1)

ball2 = Ball(450, 250, -8)
ball_group.add(ball2)
all_sprites_group.add(ball2)

ball3 = Ball(450, 350, 8)
ball_group.add(ball3)
all_sprites_group.add(ball3)

ball4 = Ball(450, 430, -8)
ball_group.add(ball4)
all_sprites_group.add(ball4)

player = Player(80,250)
player_group.add(player)
all_sprites_group.add(player)


start_menu = menu(screen)
if start_menu == 'done':
    game_over = True
elif start_menu == 'play':
    game_over = False
#end if


# ======= game loop ======= #
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True      
        #end if
    #next event

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
    elif keys[pygame.K_DOWN]:
        player.move_down()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    elif keys[pygame.K_LEFT]:
        player.move_left()
    #end if

    # -- Game logic goes after this comment
    if player.rect.x > 790 and player.rect.y > 200:
        game_over = False
    #end if


    all_sprites_group.update()

    ball_hit_wall_list = pygame.sprite.spritecollide(ball1, wall_list, False)
    ball_hit_wall_list2 = pygame.sprite.spritecollide(ball2, wall_list, False)
    ball_hit_wall_list3 = pygame.sprite.spritecollide(ball3, wall_list, False)
    ball_hit_wall_list4 = pygame.sprite.spritecollide(ball4, wall_list, False)
    if len(ball_hit_wall_list) > 0:
        ball1.change_x *= -1
    #end if
    if len(ball_hit_wall_list2) > 0:
        ball2.change_x *= -1
    #end if
    if len(ball_hit_wall_list3) > 0:
        ball3.change_x *= -1
    #end if
    if len(ball_hit_wall_list4) > 0:
        ball4.change_x *= -1
    #end if
    player_hit_ball_list = pygame.sprite.spritecollide(ball1, player_group, True)
    player_hit_ball_list2 = pygame.sprite.spritecollide(ball2, player_group, True)
    player_hit_ball_list3 = pygame.sprite.spritecollide(ball3, player_group, True)
    player_hit_ball_list4 = pygame.sprite.spritecollide(ball4, player_group, True)
    if len(player_hit_ball_list) > 0:
        player = Player(80, 250)
        player_group.add(player)
        all_sprites_group.add(player)
    #end if
    if len(player_hit_ball_list2) > 0:
        player = Player(80, 250)
        player_group.add(player)
        all_sprites_group.add(player)
    #end if
    if len(player_hit_ball_list3) > 0:
        player = Player(80, 250)
        player_group.add(player)
        all_sprites_group.add(player)
    #end if
    if len(player_hit_ball_list4) > 0:
        player = Player(80, 250)
        player_group.add(player)
        all_sprites_group.add(player)
    #end if

    player_hit_wall_list = pygame.sprite.spritecollide(player, wall_list, False)
    if len(player_hit_wall_list) > 0:
        player.set_speed(0, 0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y
    #end if

    player_old_x = player.rect.x
    player_old_y = player.rect.y

    
    # -- Screen background is BLACK
    screen.fill(WHITE)
    
    # -- Draw here
    pygame.draw.rect(screen, LIGHTGREEN, (840, 200, 140, 170))
    pygame.draw.rect(screen, LIGHTBLUE, (15, 210, 145, 200))
    all_sprites_group.draw(screen)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
