import pygame, json, random

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


file = open("Pygame/Worlds hardest game/level1.JSON", "r")
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

    def change_direction(self):
        self.change_x *= -1
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

attempts = 0
font = pygame.font.SysFont("freesansbold.ttf", 30)
def print_text(x_pos, y_pos, screen, text_string, colour):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, colour)
    screen.blit(text_map, [x_pos, y_pos])
#end procedure

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
        game_over = True
    #end if
  
    ball_hit_wall_list = pygame.sprite.groupcollide(ball_group, wall_list, False, False)
    for b in ball_hit_wall_list:
        b.change_direction()
    #end if
    

    player_hit_ball_list = pygame.sprite.groupcollide(ball_group, player_group, False, True)
    if len(player_hit_ball_list) > 0:
        player = Player(80, 250)
        player_group.add(player)
        all_sprites_group.add(player)
        attempts += 1
    #end if

    player_hit_wall_list = pygame.sprite.spritecollide(player, wall_list, False)
    if len(player_hit_wall_list) > 0:
        player.set_speed(0, 0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y
    #end if

    player_old_x = player.rect.x
    player_old_y = player.rect.y

    all_sprites_group.update()
    # -- Screen background is WHITE
    screen.fill(WHITE)
    
    
    # -- Draw here
    pygame.draw.rect(screen, LIGHTGREEN, (840, 200, 140, 170))
    pygame.draw.rect(screen, LIGHTBLUE, (15, 210, 145, 200))
    all_sprites_group.draw(screen)
    print_text(30, 30, screen, "Attempts: {}".format(attempts), RED)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    

    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()