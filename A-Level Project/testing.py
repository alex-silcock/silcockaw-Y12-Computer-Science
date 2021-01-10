import pygame 
RED = (0,0,0)
BLACK = (255, 255, 255)
WHITE = (0,0,0)
# -- Initialise PyGame
pygame.init()

# -- Blank Screen
screen_width = 1300
screen_height = 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# -- Title of window
pygame.display.set_caption("Maze Kingdom")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

#player collisions with the door
self.player_collide_door = pygame.sprite.spritecollide(self.player, self.door_group, False)
if self.door_locked == True and len(self.player_collide_door) > 0:
    self.player.set_speed(0, 0)
    self.player.rect.x = self.player_old_x1
    self.player.rect.y = self.player_old_y1

elif self.door_locked == False and len(self.player_collide_door) > 0:
    self.door.open_door()
#end if

#necessary for collisions
self.player_old_x1 = self.player.rect.x
self.player_old_y1 = self.player.rect.y