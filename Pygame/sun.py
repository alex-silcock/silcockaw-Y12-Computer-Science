import pygame

# -- Global Constants

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
pygame.display.set_caption("House")

# -- Exit game flag set to false
done = False

sun_x = 40
sun_y = 100

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # -- Game logic goes after this comment
    sun_x = sun_x + 5
    
    #resetting the value of the sun if it gets out of frame
    if sun_x > 640:
        sun_x = 40
    #endif

    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.rect(screen, (155,100,0), (235, 180, 35, 35)) #top left window
    pygame.draw.rect(screen, (155,100,0), (350, 180, 35, 35)) #top right window
    pygame.draw.rect(screen, (155,100,0), (235, 250, 35, 35)) #bottom left window
    pygame.draw.rect(screen, (155,100,0), (350, 250, 35, 35)) #bottom right window
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40,0)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()