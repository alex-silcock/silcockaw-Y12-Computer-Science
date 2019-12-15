import numpy,math,heapq,sys
from numpy.random import randint as rand

def generate(width=81, height=51, complexity=.75, density=.75):
    # Only odd dimensions
    dimension = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    complexity = int(complexity * (5 * (dimension[0] + dimension[1])))  # No. of blocks
    density = int(density * ((dimension[0] // 2) * (dimension[1] // 2)))  # Size of blocks
    Z = numpy.zeros(dimension, dtype = int)
    Z[0, :] = 1
    Z[-1, :] = 1
    Z[:, 0] = 1
    Z[:, -1] = 1
    for i in range(density):
        y = 2 * rand(0, dimension[0] // 2)
        x = 2 * rand(0, dimension[1] // 2) 
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            if x < dimension[1] - 2:
                neighbours.append((y, x + 2))
            if y > 1:
                neighbours.append((y - 2, x))
            if y < dimension[0] - 2:
                neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z

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
