import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (51, 51, 255)
YELLOW = (255, 255, 51)
RED = (255, 51, 51)
PINK = (255, 51, 133)
GREEN = (51, 255, 51)
PURPLE = (153, 51, 255)
LIGHTBLUE = (51, 255, 255)
ORANGE = (255, 51, 51)
BALLCOLOURS = (WHITE,BLUE,YELLOW,GREEN,PINK,RED,PURPLE,LIGHTBLUE)
class Ball():
    def __init__(self, x, y,screen_dimensions,colour):
        self.x = x
        self.y = y
        self.direction_y = random.randint(8,12) * random.choice([1,-1])
        self.direction_x = random.randint(8,12) * random.choice([1,-1])
        self.colour = colour
        self.size = 15
        self.width = (screen_dimensions[0],screen_dimensions[1])
        self.height = (screen_dimensions[2],screen_dimensions[3])

    def move(self):
        if self.y > self.height[1] - self.size:
            self.direction_y = abs(self.direction_y) * -1 
        elif self.y < self.height[0] + self.size:
            self.direction_y = abs(self.direction_y)
        elif self.x < self.width[0] + self.size:
            self.direction_x = abs(self.direction_x)
        elif self.x > self.width[1] - self.size:
            self.direction_x = abs(self.direction_x) * -1
                
        #End if
        self.y += self.direction_y 
        self.x += self.direction_x 

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x,self.y), self.size)

# -- Initialise PyGame
pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()
size = (info.current_w, info.current_h)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

pygame.display.set_caption("Bouncing Balls")

game_over = False
ball_size = 15
dimensions =[[],[],[],[]]
dimensions[0] = [0,size[0]//2,0,size[1]//2]
dimensions[1] = [0,size[0]//2,size[1]//2,size[1]]
dimensions[2] = [size[0]//2,size[0],0,size[1]//2]
dimensions[3] = [size[0]//2,size[0],size[1]//2,size[1]]
quadrants = [[],[],[],[]]
for i in range(4):
    for j in range(20):
        X = random.randint(dimensions[i][0],dimensions[i][1])
        Y = random.randint(dimensions[i][2],dimensions[i][3])
        e = random.choice([0,4])
        quadrants[i].append(Ball(X,Y,dimensions[i],BALLCOLOURS[i + e]))
#endfor 

### -- Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_SPACE:
                for i in range(4):
                    for j in range(11):
                        X = random.randint(dimensions[i][0],dimensions[i][1])
                        Y = random.randint(dimensions[i][2],dimensions[i][3])
                        e = random.choice([0,4])
                        quadrants[i].append(Ball(X,Y,dimensions[i],BALLCOLOURS[i + e]))
                    #endfor 
            elif event.key == pygame.K_UP:
                ball_size += 3
            elif event.key == pygame.K_DOWN:
                ball_size -= 3
            #End If
        #End If
    #Next event
    screen.fill (BLACK)
    if ball_size < 2:
        ball_size = 2
    for quadrant in quadrants:
        for circle in quadrant:
            circle.move()
            circle.size = ball_size
            circle.draw()

    pygame.display.flip()

    clock.tick(50)

#End While - End of game loop

pygame.quit()
