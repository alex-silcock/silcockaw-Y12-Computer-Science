import json
from Pygame.Maze.mazeAlgos import getNodes

file = open("Python/Shortest paths/map.JSON", "r")
maze = json.load(file)
file.close()

a = getNodes(maze)
print(a)