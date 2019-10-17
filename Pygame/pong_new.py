# -- library imports
import pygame

# -- Global Constants
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
    text = font.render("1. Press p to play", 5, BLACK)
    textRect = text.get_rect()
    textRect.center = (size[0]//2,size[1]//2)
    screen.blit(text, textRect)
    pygame.display.flip()

    running = True

    while running:
        event = pygame.event.wait()
        pygame.event.get()
        if event.type == pygame.K_p:
            print (pygame.mouse.get_pos())
            in_game = True
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

main_menu()
pygame.quit()