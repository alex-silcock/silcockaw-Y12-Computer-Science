a = int(input("Enter number"))
hundreds = a // 100
rem = a % 100
tens =  rem // 10
units = a % 10
print(a, hundreds, tens, units)