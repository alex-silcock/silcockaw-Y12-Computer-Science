#take a string input from a user and output the number of words in the string

user_string = input("Enter a sentence ")
total = 1

#for loop: 
for i in range(len(user_string)):
    #if statement: if user_string is a value add one to the total (number of words)
    if(user_string[i] == ' '):
        total += 1
    #end if
#next
print("There are",  total, "words in that sentence")
