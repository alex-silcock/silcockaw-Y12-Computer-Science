class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, radius, x_coord, y_coord):
        super().__init__()
        self.colour = colour
        
        #The radius of the ball
        self.radius = radius

        self.image = pygame.Surface([self.radius, self.radius])
        self.rect = self.image.get_rect()
        
        #the x and y coordinates of the ball
        self.rect.x = x_coord
        self.rect.y = y_coord
        

        #The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        #current angle in radians
        self.angle = 0

        #how fast to orbit in radians per frame
        self.speed = 0.005
    #end procedure

    #class methods
    def update(self):
        #Update the ball's position

        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
        self.angle += self.speed

    def draw(self):
        pygame.draw.circle(screen, self.colour, [self.rect.x, self.rect.y], self.radius)
    #end procedure
#end class