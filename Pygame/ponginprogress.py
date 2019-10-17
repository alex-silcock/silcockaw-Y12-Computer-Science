# -- library imports
import pygame

# -- Global Constants

def message(screen):
    font=pygame.font.SysFont("arial", 20)
    text = font.render("Pong Game (C) Alex Silcock", 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (size[0]//2,size[1]//2)
    screen.blit(text, textRect)
#enddef

def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
#end function

def main_menu():

    intro = True
    in_game = False

    #Font's and text
    font = pygame.font.SysFont ("arial", 60)
    text = font.render ("", True, WHITE)
    

    #Background Image
    screen.fill(WHITE)
    screen.blit(text, (size[0]//2, size[1]//2))

    #BUTTONS
    screen.blit(text, (size[0]//2 , size[1]//2))

    font = pygame.font.SysFont("arial", 80)
    text = font.render("Press p to play", 5, BLACK)
    textRect = text.get_rect()
    textRect.center = (size[0]//2,size[1]//2)
    screen.blit(text, textRect)
    pygame.display.flip()

    running = True

    while running:
        event = pygame.event.wait()
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if event.type == pygame.K_p:
            in_game = True
        #end if
        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #end if
            #next event
        #end while
#end function

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

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#defining the function of ponggame() to then overlay menus
def pong_game():
    ball_width = 20
    x_val = 150
    y_val = 200
    x_direction = 5
    y_direction = 5
    padd_length = 15
    padd_width = 60
    x_padd = 0
    y_padd = 200
    x_padd_2 = 625
    y_padd_2 = 200
    score_a = 0
    score_b = 0
    done = False
    
    def draw_score_a(screen, x, y, score):
        font = pygame.font.SysFont("arial", 20)
        text_a = font.render(str(score_a), 1, WHITE)
        screen.blit(text_a, (x, y))
    #end function

    def draw_score_b(screen, x, y, score):
        font = pygame.font.SysFont("arial", 20)
        text_b = font.render(str(score_b), 1, WHITE)
        screen.blit(text_b, (x, y))
    #end function

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
    #end function

    in_game = False

    while not done:
        if in_game == False:
            main_menu()
        elif in_game == True:
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
           
            #Next event

            # -- Game logic goes after this comment
            #ball movement
            x_val = x_val + x_direction
            y_val = y_val + y_direction

            #Making the right paddle move
            if y_padd_2 > y_val:
                y_padd_2 = y_padd_2 - 6
            elif y_padd_2 < y_val:
                y_padd_2 = y_padd_2 + 6
            #End if
        
            #if the ball goes past and the paddle hasnt hit it, then it will be reset, and the score of player b will change
            #as the opposite player has won a point
            if x_val < 0:
                clock.tick(1)
                x_val = 600
                y_val = 200
                x_direction = -5
                y_direction = 5
                score_b = score_b + 1
                
            #endif

            #doing the above but for the opposite player
            if x_val > 640 - ball_width:
                clock.tick(1)
                x_val = 40
                y_val = 200
                x_direction = 5
                y_direction = 5
                score_a = score_a + 1
                
            #endif

            #max score, if the score is 5 then the game will end
            if score_a == 5 or score_b == 5:
                done = True
            #endif

            if y_val > (size[1] - ball_width) or y_val < 0:
                y_direction = y_direction * -1
            #endif

            #collisions for left paddle, changes direction + speeds up
            if x_val < padd_length:
                if y_val > y_padd - (ball_width//2) and y_val < (y_padd + padd_width):  
                    x_direction = x_direction * -1.05
            #endif
            #collisions for right paddle
            if x_val > size[0] - (padd_width - ball_width):
                if y_val > y_padd_2 - (ball_width//2) and y_val < (y_padd_2 + padd_width):  
                    x_direction = abs(x_direction) * -1.05
            #endif

            # -- Screen background is BLACK
            screen.fill (BLACK)

            # -- Draw here
            pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
            pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
            draw_score_a(screen, 300, 30, score_a)
            draw_score_b(screen, 330, 30, score_b)
            pygame.draw.rect(screen, WHITE, (x_padd_2, y_padd_2, padd_length, padd_width))
            message(screen)
            

            # -- flip display to reveal new position of objects
            pygame.display.flip()

            # - The clock ticks over
            clock.tick(60)

        #End While - End of game loop
    #endfunction

pong_game()
pygame.quit()
