# Import libraries
import pygame
import math
import random

# Define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)

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
        
        # collisions
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
#end class

# Set game loop to false so it runs
done = False

# Create an object using the ball class
ball_list = []
colour_list = [RED, GREEN, BLUE, WHITE, YELLOW]
for count in range(20):
    x_rand = random.randrange(10, screen_width - 10)
    y_rand = random.randrange(10, screen_height - 10)
    x_speed_rand = random.randrange(1, 10)
    y_speed_rand = random.randrange(1, 10)
    colour_rand = random.choice(colour_list)
    my_ball = Ball(x_rand, y_rand, colour_rand, x_speed_rand, y_speed_rand)
    ball_list.append(my_ball)
#next count

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
    for my_ball in ball_list:
        my_ball.draw(screen)
        my_ball.move()
    #next 
    
    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
#End While

pygame.quit()