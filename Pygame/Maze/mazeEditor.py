import pygame
import json
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)

class Wall(pygame.sprite.Sprite):
    # Define the constructor 
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the constructor
        super().__init__()
        width = 10
        height = 10
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    #end procedure
#end class

# -- Initialise PyGame
pygame.init()



all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# -- Blank Screen
size = (1300,800)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False


file = open("wallgrid.JSON","r")



theMazeArray = json.load(file)
last_pressed = []
print(theMazeArray)

file.close()

for i in range (len(theMazeArray)):
    for j in range (len(theMazeArray[i])):
        if theMazeArray[i][j] == 1:
            newwall = Wall(j*10,i*10)
            wall_list.add(newwall)
            all_sprite_list.add(newwall)
        #end if
    #next j
#next i 

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_SPACE:
                for i in range (len(theMazeArray)):
                    for j in range (len(theMazeArray[i])):
                        if theMazeArray[i][j] == 1:
                            theMazeArray[i][j] = 0
                            for wall in wall_list:
                                wall.kill()
                            #next wall
                        #end if
                    #next j
                #next i
            #end if
        #end if
    #next event

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        x = pos[0]//10
        y = pos[1]//10


        if [x,y] != last_pressed:
            if theMazeArray[y][x] == 1:
                theMazeArray[y][x] = 0
                for wall in wall_list:
                    if wall.rect.collidepoint(pos):
                        wall.kill()
            elif theMazeArray[y][x] == 0:
                theMazeArray[y][x] = 1
            #end if
            last_pressed = [x,y]
        #end if
    #end if
    

    # -- Game logic goes after this comment

    pos = pygame.mouse.get_pos()
    
    
    for i in range (len(theMazeArray)):
        for j in range (len(theMazeArray[i])):
            if theMazeArray[i][j] == 1:
                newwall = Wall(j*10,i*10)
                wall_list.add(newwall)
                all_sprite_list.add(newwall)  
            #end if
        #next j
    #next i  


    # -- Screen background is BLACK

    all_sprite_list.update()
    screen.fill (BLACK)
    all_sprite_list.draw(screen)
    # -- Draw here

    all_sprite_list.update()
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
     # - The clock ticks over
    clock.tick(144)
#End While - End of game loop
pygame.quit()

# Opening the json file which stores the map, and writing ("w+") to it
mazeFile = open("wallgrid.JSON", "w+")
json.dump(theMazeArray, mazeFile)
mazeFile.close()