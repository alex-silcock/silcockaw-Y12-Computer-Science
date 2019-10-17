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


#to have moving balls on the front screen
    first_cube_x = 100
    first_cube_y = 100
    second_cube_x = 100
    second_cube_y = 320
    third_cube_x = 100
    third_cube_y = 392
    fourth_cube_x = 100
    fourth_cube_y = 420

    x_direction = 5
    y_direction = 5

    pygame.draw.rect(screen, BLACK, (first_cube_x, first_cube_x, 10, 10))
    pygame.draw.rect(screen, BLACK, (second_cube_x, second_cube_y, 10, 10))
    pygame.draw.rect(screen, BLACK, (third_cube_x, third_cube_y, 10, 10))
    pygame.draw.rect(screen, BLACK, (fourth_cube_x, fourth_cube_y, 10, 10))

    first_cube_x = first_cube_x + x_direction
    first_cube_y = first_cube_y + y_direction
    second_cube_x = second_cube_x + x_direction
    second_cube_y = second_cube_y + y_direction
    third_cube_x = third_cube_x + x_direction
    third_cube_y = third_cube_y + y_direction
    fourth_cube_x = fourth_cube_x + x_direction
    fourth_cube_y = fourth_cube_y + y_direction
