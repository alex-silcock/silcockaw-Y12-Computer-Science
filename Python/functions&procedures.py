#a procedure as no value is returned
#x,y are parameters
def multiply(x,y):
    print(x * y)
#endprocedure

#2,5 are arguments 
multiply(2,5)

#a function as a value is returned
def multiplication(x,y):
    product = (x * y)
    return product
#endfunction

a = multiplication(6,8)
print(a)