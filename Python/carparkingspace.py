parkingspace = [
    #10 rows, 6 columns
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ["empty","empty","empty","empty","empty","empty"],
    ]

#taking inputs
plate = str(input("Please enter your number plate "))

row = int(input("Please enter your row "))
while row > 10:
    print("Invalid row entry (Entry should be between 1 and 10) ")
    row = int(input("Please enter your row "))
#endwhile
space = int(input("Please enter your space "))

while space > 6:
    print("Invalid space entry")
    space = int(input("Please enter your space (Entry should be between 1 and 6) "))
#enwhile

#subtracting 1 from row and space so they equal the correct position in the array
row = row - 1
space = space - 1

#using an if statement - if the place is not empty then print space is taken
#outputs the arrays of the parking spaces 
if parkingspace[row][space] == "empty":
    parkingspace[row][space] = plate
else:
    print("This space is taken")
print(parkingspace)
