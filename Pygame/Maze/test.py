from mazeAlgos import getNodes
import json
file = open("Pygame/Shortest paths/map.JSON", "r")
maze = json.load(file)
file.close()

a = getNodes(maze)
print(a)
