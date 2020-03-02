import json

myarray = [[0 for i in range(130)] for j in range(80)]

file = open("wallgrid.JSON","w")
json.dump(myarray,file)
file.close