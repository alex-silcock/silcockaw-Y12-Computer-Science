# Import libraries
import pygame
import math
import random

# Define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (0,0,0)
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
    def __init__(self, x, y, col, x_speed, y_speed):
        # --- Class Attributes ---
        # Ball position
        self.x = x
        self.y = y

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
        self.x += self.change_x
        self.y += self.change_y
        if self.x >= screen_width - self.size:
            self.change_x *= -1
        elif self.x <= 0 + self.size:
            self.change_x *= -1
        elif self.y >= screen_height - self.size:
            self.change_y *= -1
        elif self.y <= 0 + self.size:
            self.change_y *= -1
        #end if
    #end proc
        

    # Draws the ball on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    #end proc

# Set game loop to false so it runs
done = False

# Create an object using the ball class
theBall = Ball(100, 100, RED, 3, 3) 
theBall_2 = Ball(200,200, BLUE, 3, 3)
theBall_3 = Ball(300,300, YELLOW, 3, 3)


# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    
    # Clear the screen
    screen.fill(WHITE)

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