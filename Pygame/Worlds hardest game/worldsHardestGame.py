import pygame
import json

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
pygame.display.set_caption("World's Hardest Game")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


file = open("Pygame/Worlds hardest game/whg_map.JSON", "r")
theMazeArray = json.load(file)
last_pressed = []
file.close()



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
        self.size = 20
        self.color = BLUE
        self.change_x = x_speed

        self.x = x_coord
        self.y = y_coord
    #end procedure

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    #end procedure 

    def update(self):
        self.x += self.change_x
#end class

ball_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

for i in range (len(theMazeArray)):
    for j in range (len(theMazeArray[i])):
        if theMazeArray[i][j] == 1:
            newwall = Wall(j*10,i*10)
            wall_list.add(newwall)
            all_sprites_group.add(newwall)
        #end if
    #next j
#next i 

ball = Ball(450, 370, 3)
ball_group.add(ball)



# ======= game loop ======= #
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True      
        #end if
    #next event

    # -- Game logic goes after this comment
    all_sprites_group.update()
    ball_hit_wall_list = pygame.sprite.spritecollide(ball, wall_list, False)

    
    # -- Screen background is BLACK
    screen.fill(WHITE)
    
    # -- Draw here
    all_sprites_group.draw(screen)
    ball.draw(screen)
    ball.update()
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
