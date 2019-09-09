
#define a function "print_factors" to calculate the factors
def print_factors(x):
    
    print("The factors of", x , "are:")
    #loop: loops through every value and if x divided by the counter of the loop has a modulo value of 0 then it's a factor
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    #next

num = int(input("Enter a number: "))

print_factors(num)
