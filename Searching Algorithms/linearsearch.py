import json

file = open("Searching Algorithms/names.txt", "r")
namelist = json.load(file)

def linearSearch(namelist, nameSought):
    index = -1
    count = 0
    found = False
    while count < len(namelist) and not found:
        if namelist[count] == nameSought:
            index = count
            found = True
        #end if
        count = count + 1
    #end while
    return index
#end function

# main prog

nameSought = input("Enter name for searching ")
index_of_name = linearSearch(namelist, nameSought)
print("Position of name : " , index_of_name + 1)
