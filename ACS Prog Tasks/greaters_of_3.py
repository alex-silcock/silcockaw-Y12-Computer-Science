#creating a max variable to assign to the highest number
max = -1000
count = 1

#take 3 user input integers

int1 = int(input("Enter your first number "))
int2 = int(input("Enter your second number "))
int3 = int(input("Enter your third number "))



#determine which number is the greatest by using a for loop
for count in range (1,3):
    if int1 > max:
        max = int1
    elif int2 > max:
        max = int2
    elif int3 > max:
        max = int3

print("The highest of the three numbers was", max)


