# Import libraries
import pygame
import math
import random

# Define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define the class Ball
class Ball():
    # Constructor function to define initial state of a ball object
    def __init__(self, x, y, col, x_speed, y_speed, ballarea):
        # --- Class Attributes ---
        # Ball position
        self.x = x
        self.y = y
        self.court = ballarea

        # Ball's vector
        self.change_x = x_speed
        self.change_y = y_speed

        # Ball Size
        self.size = 10

        # Ball colour
        self.color = col
    #end proc

    # -- Class Methods ---
    # Defines the ball's movement
    def move(self):
        if self.x <= (self.court[0] + self.size) or self.x >= (self.court[2] - self.size):
            self.change_x *= -1
        #end if

        if self.y <= (self.court[1] + self.size) or self.y >= (self.court[3] - self.size):
            self.change_y *= -1
        #end if

        self.x += self.change_x
        self.y += self.change_y
        #end if
    #end proc
        
    # Draws the ball on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    #end proc
#end class

# Set game loop to false so it runs
done = False

# Create an object using the ball class
theBallarea = (0,0,300,200)
theBallarea2 = (200,200,500,300)
theBallarea3 = (350,350,700,400)

theBall = Ball(20,20, RED, 3, 3, theBallarea) 
theBall_2 = Ball(240,250, BLUE, 3, 3, theBallarea2)
theBall_3 = Ball(370,370, YELLOW, 3, 3, theBallarea3)

# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball on the screen and then move it on
    theBall.draw(screen)
    theBall.move()
    theBall_2.draw(screen)
    theBall_2.move()
    theBall_3.draw(screen)
    theBall_3.move()

    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
#End While

pygame.quit()