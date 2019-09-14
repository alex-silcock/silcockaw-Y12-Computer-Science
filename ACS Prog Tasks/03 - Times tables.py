#Taking an integer input, 1 to 10, from user and outputting times table up to 12

#using "a" for the for loop

a = 0

#Asking user for input

num1 = int(input("Enter a number from 1 to 10 "))

#While loop if number is outside 1,10 - retakes the input

while num1 < 1 or num1 > 10:
    
    #if number is out of range: output error message, retake input
    
        print("Value out of range: re-enter value")
        num1 = int(input())
        
    #if number is valid then outputs times tables
        
if num1 <= 10:
    for a in range (1, 13):
        print(num1, "x", a, "=", num1 * a)
        a += 1
        
#endwhile


###ACS - No need to set a at the beginning of the prgram in the case .. the for loop does that.
###ACS - I think your end while is in the wrong place and there is no #Next at the end of the for loop
