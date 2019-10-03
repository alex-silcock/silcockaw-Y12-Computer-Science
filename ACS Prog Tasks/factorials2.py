#defining the function as a value is going to be returned

def fact(num):
    #result = 1
    if num == 0:
        result = 1
    else:
        result = num * fact(num - 1)
    #endif
    return result
#end function

#main program
inp = int(input("Enter number to find factorial of "))
answer = fact(inp)
print(answer)