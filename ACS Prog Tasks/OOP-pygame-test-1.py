import pygame
import random
from typing import Tuple

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

### What is a class?
### A class is a blueprint / template for an object which defines its attributes and methods
### Attributes is like the data of the class, whereas the methods are the functions that the 
### object carries out
 
class Block(pygame.sprite.Sprite):
    def __init__(self, colour:Tuple[int], width:int, height:int): ### What is this subroutine known as?
        ### This subroutine is known as constructor. it's used to instantiate the object
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour) 
        self.rect = self.image.get_rect()
    #end procedure
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
    #end procedure
    
    def update(self):
        self.rect.y += 3
        if self.rect.y > screen_height:
            self.reset_pos()
        #end if
    #end procedure
#end class



 
### Fix this class so that it inherits Block and is the colour RED
class Player(Block):
    def __init__(self, colour:Tuple[int], width, height):
        super().__init__(colour, width, height)
        self.image.fill(RED)

    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
     #end procedure
#end class
        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width:int = 700
screen_height:int = 400
screen:Tuple[int] = pygame.display.set_mode([screen_width, screen_height])
 
block_list:list = pygame.sprite.Group()
 
all_sprites_list:list = pygame.sprite.Group()
 

### Create 50 random positioned blocks that will be displayed
for i in range(50):
    block = Block(BLACK, 10, 10)
    block.reset_pos()
    block_list.add(block)
    all_sprites_list.add(block)

 
# Create a red player 
player = Player(RED, 10, 10)
all_sprites_list.add(player)

game_over:bool = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score:int = 0
 
# -------- Main Program Loop -----------
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    
    all_sprites_list.update() ### What OOP concept is being used here? Encapsulation
 
    # See if the player has collided with a block.
    player_block_collision = pygame.sprite.spritecollide(player, block_list, True)
    # Update the score +1 for every block collision
    if len(player_block_collision) > 0:
        score += 1

    # Draw all the sprites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()

