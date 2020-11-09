import pygame, math
level1Finished = False
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
LIGHTGREEN = (100,255,100)
LIGHTBLUE = (100,100,255)
coloursList = [BLACK, WHITE, BLUE, YELLOW, RED, LIGHTGREEN, LIGHTBLUE]
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (1300, 800)
screen = pygame.display.set_mode(size)
# -- Title of window
pygame.display.set_caption("Maze Kingdom")
# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, size, x_coord, y_coord, center_x_orbit, center_y_orbit, sizeOfOrbit):
        super().__init__()
        self.colour = colour

        #the size of the ball
        self.size = size

        #the size of the orbit
        self.sizeOfOrbit = sizeOfOrbit

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
        #the x and y coordinates of the ball
        self.rect.x = x_coord
        self.rect.y = y_coord

        #the "center" the sprite will orbit
        self.center_x = center_x_orbit
        self.center_y = center_y_orbit

        #current angle in radians
        self.angle = 0

        #how fast to orbit in radians per frame
        self.speed = 0.08
    #end procedure

    #class methods
    def update(self):
        #Update the ball's position

        # Calculate a new x, y
        self.rect.x = self.sizeOfOrbit * math.sin(self.angle) + self.center_x
        self.rect.y = self.sizeOfOrbit * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed

    def draw(self):
        pygame.draw.circle(screen, RED, [self.rect.x, self.rect.y], self.size)
    #end procedure
#end class

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, size, x_coord, y_coord, center_x_orbit, center_y_orbit, sizeOfOrbit):
        super().__init__()
        self.colour = colour

        #the size of the ball
        self.size = size

        #the size of the orbit
        self.sizeOfOrbit = sizeOfOrbit
        self.image = pygame.Surface([self.size, self.size])
        #the x and y coordinates of the ball
        self.rect.x = x_coord
        self.rect.y = y_coord

        #the "center" the sprite will orbit
        self.center_x = center_x_orbit
        self.center_y = center_y_orbit

        #current angle in radians
        self.angle = 0

        #how fast to orbit in radians per frame
        self.speed = 0.08
    #end procedure

    #class methods
    def update(self):
        #Update the ball's position

        # Calculate a new x, y
        self.rect.x = self.sizeOfOrbit * math.sin(self.angle) + self.center_x
        self.rect.y = self.sizeOfOrbit * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed

    def draw(self):
        pygame.draw.ellipse(screen, RED, [self.rect.x, self.rect.y], self.size)
    #end procedure
#end class


all_sprites_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

ball = Ball(RED, 30, 0, 0, size[0]//2, size[1]//2, 30)
all_sprites_group.add(ball)
ball_group.add(ball)


while not level1Finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            level1Finished = True
            pygame.quit()

    screen.fill(BLACK)
    all_sprites_group.update()
    all_sprites_group.draw(screen)
    
    #game updates inside the loop 
    
    pygame.display.flip()
    clock.tick(60) 


class InputBox:
    # text box to enter name
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable to allow the user to type
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.name = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


