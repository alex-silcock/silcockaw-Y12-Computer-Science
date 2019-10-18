# -- library imports
import pygame

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

def new_screen(screen):
    finished = False
    while finished == False:
        screen.fill(WHITE)
        how_to_play(screen)
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_ESCAPE]:
                main_menu()
            #end if
        #next event
    #end while
#end def


def message(screen):
    font = pygame.font.SysFont("arial", 20)
    text = font.render("Pong Game (C) Alex Silcock", 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (size[0]//2, size[1]//2)
    screen.blit(text, textRect)
# enddef

def how_to_play(screen):
    font_1 = pygame.font.SysFont("Moon 2.0", 40)
    text_1 = font_1.render("Use up and down to move the left paddle", 5, BLACK)
    textRect_leftpaddle = text_1.get_rect()
    textRect_leftpaddle.center = (size[0]//2, size[1]//2)
    screen.blit(text_1, textRect_leftpaddle)

    font_2 = pygame.font.SysFont("Moon 2.0", 40)
    text_2 = font_2.render("Use w and s to move the right paddle", 5, BLACK)
    textRect_rightpaddle = text_2.get_rect()
    textRect_rightpaddle.center = (size[0]//2, 300)
    screen.blit(text_2, textRect_rightpaddle)
#end def



def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
# end function


def main_menu(screen):
    finished = False
    textcolour = BLACK
    textcolour_2 = BLACK
    textcolour_3 = BLACK
    speed_computer = 6
    
    while finished == False:
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

        mouse = pygame.mouse.get_pos()

        font = pygame.font.SysFont("helveltica", 80)
        text = font.render("SINGLEPLAYER", 5, textcolour)
        textRect = text.get_rect()
        textRect.center = (size[0]//2, 200)
        screen.blit(text, textRect)

        font_2 = pygame.font.SysFont("helveltica", 80)
        text_2 = font.render("MULTIPLAYER", 5, textcolour_2)
        textRect_2 = text_2.get_rect()
        textRect_2.center = (size[0]//2, 260)
        screen.blit(text_2, textRect_2)

        font_3 = pygame.font.SysFont("helveltica", 80)
        text_3 = font.render("HOW TO PLAY", 5, textcolour_3)
        textRect_3 = text_3.get_rect()
        textRect_3.center = (size[0]//2, 320)
        screen.blit(text_3, textRect_3)

        # BUTTONS
        if textRect.collidepoint(mouse):
            textcolour = RED
        else:
            textcolour = BLACK
        if textRect_2.collidepoint(mouse):
            textcolour_2 = RED
        else:
            textcolour_2 = BLACK
        if textRect_3.collidepoint(mouse):
            textcolour_3 = RED
        else:
            textcolour_3 = BLACK
        #end if

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if textRect.collidepoint(mouse):
                    finished = True
                    msg = 'singleplayer'
                elif textRect_2.collidepoint(mouse):
                    finished = True
                    msg = 'multiplayer'
                elif textRect_3.collidepoint(mouse):
                    finished = True
                    msg = 'how to play'
                #end if
            #end if
        #next event
    
    if msg == 'how to play':
        new_screen(screen)
    else:
        pong_game(msg, speed_computer)
# end function

#========================================= pong singleplayer =============================================#
def pong_game(mode,computerspeed):
    
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
        ball_color = BLUE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                return game_over
        #End If

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            left_y = left_y - 8
            if left_y < 0:
                left_y = 0
        elif keys[pygame.K_DOWN]:
            left_y = left_y + 8
        #end if
        if keys[pygame.K_ESCAPE]:
            mode = main_menu()
        #end if

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
        if mode == 'singleplayer':
            if right_y > y_val:
                right_y = right_y - computerspeed
            elif right_y < y_val:
                right_y = right_y + computerspeed
            # End if
        elif mode == 'multiplayer':
            if keys[pygame.K_w]:
                right_y = right_y - 8
                if right_y < 0:
                    right_y = 0
                #end if
            elif keys[pygame.K_s]:
                right_y = right_y + 8
            #end if
        #end if



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
        #endif

        #making ball bounce
        if y_val > (size[1] - ball_width) or y_val < 0:
            y_direction = y_direction * -1
        # endif
        
        # collisions for left paddle, changes direction + speeds up
        if x_val < padd_width:
            if y_val > left_y - (ball_width//2) and y_val < (left_y + padd_height):
                x_direction = x_direction * -1.05
                ball_color = RED
            #end if
        #end if
        # collisions for right paddle
        if x_val > size[0] - (padd_height - ball_width):
            if y_val > right_y - (ball_width//2) and y_val < (right_y + padd_height):
                x_direction = abs(x_direction) * -1.05
                ball_color = YELLOW
        # endif

        # -- Screen background is BLACK
        screen.fill(BLACK)

        # -- Draw here
        pygame.draw.rect(screen, ball_color, (x_val, y_val, ball_width, ball_width))
        pygame.draw.rect(screen, WHITE, (left_x, left_y, padd_width, padd_height))
        draw_score_a(screen, size[0]//2 - 20, 30, score_a)
        draw_score_b(screen, size[0]//2 + 20, 30, score_b)
        pygame.draw.rect(screen, WHITE, (right_x, right_y, padd_width, padd_height))
        message(screen)

        # -- flip display to reveal new position of objects
        pygame.display.flip()
        clock.tick(60)
    main_menu()
#end function


# ====== Main Program ====== #
in_game = False
game_over = False

main_menu()
# - The clock ticks over
clock.tick(60)
pygame.quit()
