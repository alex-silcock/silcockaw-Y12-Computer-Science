import pygame

# -- Global Constants
ball_width = 20
x_val = 150
y_val = 200
x_direction = 4
y_direction = 4
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 200
x_padd_2 = 625
y_padd_2 = 200
score_a = 0
score_b = 0

def draw_score_a(screen, x, y, score):
    font = pygame.font.SysFont("arial", 20)
    text_a = font.render(str(score_a), 1, WHITE)
    
    screen.blit(text_a, (x, y))
#enddef
def draw_score_b(screen, x, y, score):
    font = pygame.font.SysFont("arial", 20)
    text_b = font.render(str(score_b), 1, WHITE)
    screen.blit(text_b, (x, y))
#enddef

def endmessage(screen, x, y):
    font=pygame.font.SysFont("arial", 20)
    text = font.render("MMM", 1, WHITE)
    screen.blit(text, (x, y))

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
        
    keys = pygame.key.get_pressed()
    # -- the up key or down key has been pressed
    if keys[pygame.K_UP]:
        # -- write logic that happens on key press here
        y_padd = y_padd - 5
        if y_padd < 0:
            y_padd = 0
    elif keys[pygame.K_DOWN]:
        y_padd = y_padd + 5
        if y_padd > (size[1] - padd_length):
            y_padd = (size[1] - padd_length)
                # -- write logic that happens on key press here
            #End If
        #End If
    keys = pygame.key.get_pressed()
    # -- the w(up) key or s(down) key has been pressed
    if keys[pygame.K_w]:
        # -- write logic that happens on key press here
        y_padd_2 = y_padd_2 - 5
    elif keys[pygame.K_s]:
        y_padd_2 = y_padd_2 + 5
            # -- write logic that happens on key press here
            #End If
        #End If
    #Next event

    # -- Game logic goes after this comment
    #ball movement
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    #making the ball "bounce"
    if x_val > (size[0] - ball_width):
       x_direction = x_direction * -1
    #endif

    #if the ball goes past and the paddle hasnt hit it, then it will be reset, and the score of player b will change
    #as the opposite player has won a point
    if x_val < 0:
        x_val = 150
        y_val = 200
        x_direction = 4
        y_direction = 4
        score_b = score_b + 1
        x_padd = 0
        y_padd = 200
        x_padd_2 = 625
        y_padd_2 = 200
    #endif

    #doing the above but for the opposite player
    if x_val > 640 - ball_width:
        x_val = 150
        y_val = 200
        x_direction = 4
        y_direction = 4
        score_a = score_a + 1
        x_padd = 0
        y_padd = 200
        x_padd_2 = 625
        y_padd_2 = 200

    #max score, if the score is 5 then the game will end
    if score_a == 5 or score_b == 5:
        done = True
        
    #endif

    if y_val > (size[1] - ball_width) or y_val < 0:
       y_direction = y_direction * -1
    #endif

    #collisions, changes direction + speeds up
    if (y_val < y_padd + padd_width and y_val > y_padd) and x_val <= ball_width:
        x_direction = x_direction * -1
        x_direction = x_direction + 1
    #endif
    if (y_val < y_padd_2 + padd_width and y_val > y_padd_2) and x_val >= (size[0] - 40):
        x_direction = x_direction * -1
        x_direction = x_direction + 1

    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    draw_score_a(screen, 300, 30, score_a)
    draw_score_b(screen, 330, 30, score_b)
    pygame.draw.rect(screen, WHITE, (x_padd_2, y_padd_2, padd_length, padd_width))
    endmessage(screen, (size[0] / 2), (size[1] / 2))
    

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()