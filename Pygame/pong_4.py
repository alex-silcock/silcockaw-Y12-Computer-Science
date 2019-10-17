# -- library imports
import pygame
import pygame.font

# -- Global Constants
# -- Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (204,0,0)

# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

def message(screen):
    font = pygame.font.SysFont("arial", 20)
    text = font.render("Pong Game (C) Alex Silcock", 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (size[0]//2, size[1]//2)
    screen.blit(text, textRect)
# enddef


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
# end function


def main_menu():
    finished = False
    textcolour = BLACK
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    finished = True
                #end if
            #end if
        #next event
        # Background Image
        screen.fill(WHITE)

        font = pygame.font.SysFont("helveltica", 80)
        text = font.render("PLAY", 5, textcolour)
        mouse = pygame.mouse.get_pos()
        
        # BUTTONS

        textRect = text.get_rect()
        textRect.center = (size[0]//2, size[1]//2)
        screen.blit(text, textRect)
        if textRect.collidepoint(mouse):
            textcolour = RED
        else:
            textcolour = BLACK
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if textRect.collidepoint(mouse):
                    finished = True
                #end if
            #end if
        #next event
    #end while
# end function



def pong_game():
    
    ball_width = 20
    x_val = 150
    y_val = 200
    speed = 5
    x_direction = speed
    y_direction = speed
    padd_width = 15
    padd_height = 60
    left_x = 0
    left_y = 200
    right_x = 625
    right_y = 200
    score_a = 0
    score_b = 0

    def draw_score_a(screen, x, y, score):
        font = pygame.font.SysFont("arial", 20)
        text_a = font.render(str(score_a), 1, WHITE)
        screen.blit(text_a, (x, y))
    # end function

    def draw_score_b(screen, x, y, score):
        font = pygame.font.SysFont("arial", 20)
        text_b = font.render(str(score_b), 1, WHITE)
        screen.blit(text_b, (x, y))
    # end function

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
    # end function

    

    # ============ end of defining functions ============ #
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                return game_over
        #End If
    
        keys = pygame.key.get_pressed()
        # -- the up key or down key has been pressed
        if keys[pygame.K_UP]:
         # -- write logic that happens on key press here
            left_y = left_y - 5
            if left_y < 0:
                left_y = 0
        elif keys[pygame.K_DOWN]:
            left_y = left_y + 5
        
        if left_y > (size[1] - padd_height):
            left_y = size[1] - padd_height
        elif right_y > (size[1] - padd_height):
            right_y = size[1] - padd_height
            #End If
        #End If

        # -- Game logic goes after this comment
        # ball movement
        x_val = x_val + x_direction
        y_val = y_val + y_direction

        # Making the right paddle move
        if right_y > y_val:
            right_y = right_y - 6
        elif right_y < y_val:
            right_y = right_y + 6
        # End if

        # if the ball goes past and the paddle hasn't hit it, then it will be reset, and the score of player b will change
        # as the opposite player has won a point
        if x_val < 0:
            clock.tick(1)
            x_val = 600
            y_val = 200
            x_direction = speed * -1
            y_direction = speed
            score_b = score_b + 1
        # endif

        # doing the above but for the opposite player
        if x_val > 640 - ball_width:
            clock.tick(1)
            x_val = 40
            y_val = 200
            x_direction = speed
            y_direction = speed
            score_a = score_a + 1
        # endif

        # max score, if the score is 5 then the game will end
        if score_a == 5 or score_b == 5:
            game_over = False
            return game_over
        # endif

        if y_val > (size[1] - ball_width) or y_val < 0:
            y_direction = y_direction * -1
        # endif

        # collisions for left paddle, changes direction + speeds up
        if x_val < padd_width:
            if y_val > left_y - (ball_width//2) and y_val < (left_y + padd_height):
                x_direction = x_direction * -1.05
        # endif
        # collisions for right paddle
        if x_val > size[0] - (padd_height - ball_width):
            if y_val > right_y - (ball_width//2) and y_val < (right_y + padd_height):
                x_direction = abs(x_direction) * -1.05
        # endif

        # -- Screen background is BLACK
        screen.fill(BLACK)

        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
        pygame.draw.rect(screen, WHITE, (left_x, left_y, padd_width, padd_height))
        draw_score_a(screen, size[0]//2 - 20, 30, score_a)
        draw_score_b(screen, size[0]//2 + 20, 30, score_b)
        pygame.draw.rect(screen, WHITE, (right_x, right_y, padd_width, padd_height))
        message(screen)

        # -- flip display to reveal new position of objects
        pygame.display.flip()
        clock.tick(60)
#end function



in_game = False
game_over = False

while not game_over:
    main_menu()
    game_over = pong_game()
    #end if
# End While - End of game loop

# - The clock ticks over
clock.tick(60)
pygame.quit()
