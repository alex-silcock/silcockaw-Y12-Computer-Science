import pygame

map = [[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]]

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

## -- Define the class tile which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure
#end class

# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if map[x][y] == 1:
        my_wall = Tile(BLUE, 20, 20, x*20, y *20)
        wall_list.add(my_wall)
        all_sprites_list.add(my_wall)


