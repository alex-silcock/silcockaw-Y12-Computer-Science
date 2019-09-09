#takes an input of a time eg. 1:30:25 (hours, minutes, seconds) and outputs it in seconds

user_hours = int(input("Input the hours "))
user_minutes = int(input("Input the minutes "))
user_seconds = int(input("Input the seconds "))

#printing the total in seconds

print((user_hours * 3600) + (user_minutes * 60) + (user_seconds))
