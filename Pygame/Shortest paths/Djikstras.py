import pygame
import json, math

# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
BROWN = (100,100,0)
RED = (255,0,0)

game_over = False

pygame.init()

size = (500,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Djikstras Algorithm")

clock = pygame.time.Clock()

file = open("Pygame/Shortest paths/map.JSON","r")
theMazeArray = json.load(file)
file.close()

file = open("Pygame/Shortest paths/graph.JSON", "r")
graph = json.load(file)
file.close()

graph = graph


def getNodes(Maze):
    Node_List = []
    for y in range(len(Maze)):
        for x in range(len(Maze[y])):
            if Maze[y][x] == 0:
                neighbours = [0,0,0,0]                   #left,right,above,below
                if y > 0 and y < len(Maze)-1:
                    if Maze[y-1][x]== 0: neighbours[2] = 1
                    if Maze[y+1][x]== 0: neighbours[3] = 1
                if x > 0 and x < len(Maze[y])-1:
                    if Maze[y][x-1]== 0: neighbours[0] = 1
                    if Maze[y][x+1] == 0: neighbours[1] = 1
                if neighbours.count(1) > 2:
                    Node_List.append([x,y])
                elif neighbours[0] ^ neighbours[1] and neighbours[2] ^ neighbours[3]:
                    Node_List.append([x,y])
    return Node_List

def getConnections(Maze,Nodes):
    Adjacency_Vector = [[] for i in range(len(Nodes))]   #Adjacency_Vector is a list of lists of coordinates and weights
    for i in range(len(Nodes)):
        x = Nodes[i][0]
        y = Nodes[i][1]
        if Maze[y-1][x]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                y -= 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([(Nodes.index([x,y])),count])
                    Found = True
            y = Nodes[i][1]
            x = Nodes[i][0]
        if Maze[y+1][x]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                y += 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([(Nodes.index([x,y])),count])
                    Found = True
            y = Nodes[i][1]
            x = Nodes[i][0]
        if Maze[y][x-1]== 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                x -= 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([(Nodes.index([x,y])),count])
                    Found = True
            x = Nodes[i][0]
            y = Nodes[i][1]
        if Maze[y][x+1] == 0:
            Found = False
            count = 0
            while Maze[y][x] != 1 and Found == False:
                x += 1
                count += 1
                if [x,y] in Nodes:
                    Adjacency_Vector[i].append([(Nodes.index([x,y])),count])
                    Found = True
            x = Nodes[i][0]
            y = Nodes[i][1]
    Connection_Dict = {i:{} for i in range(len(Nodes))}
    for i in range(len(Adjacency_Vector)):
        for j in Adjacency_Vector[i]:
            Connection_Dict[i][j[0]] = j[1]
    return Connection_Dict    #list for each node containing lists of index of connecting node and distance

def Dijkstra(graph,start_node,end_node):
    shortest_distance = {}
    Path = []
    previous = {}
    unseen_nodes = graph
    for node in unseen_nodes:
        shortest_distance[node] = math.inf
    shortest_distance[start_node] = 0
    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node
        for Edge, Weight in graph[min_node].items():
            if Weight + shortest_distance[min_node] < shortest_distance[Edge]:
                shortest_distance[Edge] = Weight + shortest_distance[min_node]
                previous[Edge] = min_node
        unseen_nodes.pop(min_node)
    current_node = end_node
    while current_node != start_node:
        Path.insert(0,current_node)
        current_node = previous[current_node]  
    Path.insert(0,start_node)
    if shortest_distance[end_node] != math.inf:
        return Path

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.wall_group = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.player = Player(30,30,8,8)
        self.player_group.add(self.player)
        self.all_sprites_group.add(self.player)
        
        for i in range (len(theMazeArray)):
            for j in range (len(theMazeArray[i])):
                if theMazeArray[i][j] == 1:
                    self.newwall = Wall(j*10,i*10)
                    self.wall_group.add(self.newwall)
                    self.all_sprites_group.add(self.newwall)
                #end if
            #next j
        #next i
    #end procedure
    
    def update(self):
        self.all_sprites_group.update()
        self.all_sprites_group.draw(screen)

        #player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()
        #end if

        self.player_hit_wall_group = pygame.sprite.spritecollide(self.player, self.wall_group, False)
        if len(self.player_hit_wall_group) > 0:
            self.player.set_speed(0, 0)
            self.player.rect.x = self.player_old_x
            self.player.rect.y = self.player_old_y
        #end if

        self.player_old_x = self.player.rect.x
        self.player_old_y = self.player.rect.y
    #end procedure
#end class


class Player(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.speed = 2
    #end procedure

    def move_up(self):
        self.rect.y -= self.speed
    #end procedure

    def move_down(self):
        self.rect.y += self.speed
    #end procedure
 
    def move_right(self):
        self.rect.x += self.speed
    #end procedure

    def move_left(self):
        self.rect.x -= self.speed
    #end procedure

    def set_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.x += y_val
    #end procedure
#end class

            
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        width = 10
        height = 10
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    #end procedure
#end class

game = Game()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True      
        #end if
    #next event
    nodes = getNodes(theMazeArray)
    connections = getConnections(theMazeArray, nodes)
    screen.fill(BLACK)
    
    game_over = game.update()

    pygame.display.flip()
    clock.tick(60)
#end while
pygame.quit()

