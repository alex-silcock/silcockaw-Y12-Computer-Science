namelist = ["Amelia", "Ava", "Brave", "Krystal", "Precious", "Wonderful"]

def binarySearch(namelist, itemSought):
    found = False
    index = -1
    first = 0
    last = len(namelist)-1
    while first <= last and not found:
        midpoint = int((first + last) / 2)
        if namelist[midpoint] == itemSought:
            found = True
            index = midpoint
        else:
            if namelist[midpoint] < itemSought:
                first = midpoint + 1
            else:
                last = midpoint - 1
            #end if
        #end if
    #end while
    return index #index is -1 if not found
#end function

# main prog

nameSought = input("Enter name for searching ")
index_of_name = binarySearch(namelist, nameSought)
print("Position of name : " , index_of_name + 1)
