import pygame
#for second player 
keys = pygame.key.get_pressed()
# -- the w(up) key or s(down) key has been pressed
if keys[pygame.K_w]:
# -- write logic that happens on key press here
    y_padd_2 = y_padd_2 - 5
elif keys[pygame.K_s]:
    y_padd_2 = y_padd_2 + 5
# -- write logic that happens on key press here
#End If
