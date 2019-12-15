import json

myarray = [[0 for i in range(50)] for j in range(50)]

file = open("wallgrid.JSON","w")
json.dump(myarray,file)
file.close