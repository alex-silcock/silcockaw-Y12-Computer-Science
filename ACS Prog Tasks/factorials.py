#defining the function as a value is going to be returned

def fact(num):
    result = 1
    for count in range(1, num + 1):
        result = result * count
    #next count
    return result
#end function

#main program

inp = int(input("Enter number to find factorial of "))
answer = fact(inp)
print(answer)