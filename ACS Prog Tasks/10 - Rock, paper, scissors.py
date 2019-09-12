#importing random to generate a random number from 1 to 3 to play against user_choice
import random

user_choice = input("Enter Rock(R), Paper(P) or Scissors(S) ")

#while loop to make sure that the length of input is only 1 character long
while len(user_choice) > 1:
    print("Input not in correct format, try again.")
    user_choice = input("Enter Rock(R), Paper(P) or Scissors(S) ")
#end while

computer_choice = random.randint(1,3)

#if statement to convert computer choice to rock, paper or scissors
if computer_choice == 1:
    computer_choice = "Rock"
elif computer_choice == 2:
    computer_choice = "Paper"
else: computer_choice = "Scissors"
#end if

print("The computer chose", computer_choice)

#if statement to decide who wins, user or computer using the rules of rock, paper, scissors

if user_choice == 'R' and computer_choice == "Rock":
    print("Draw")
elif user_choice == 'R' and computer_choice == "Paper":
    print("You lose")
elif user_choice == 'R' and computer_choice == "Scissors":
    print("You win")
elif user_choice == 'P' and computer_choice == "Paper":
    print("Draw")
elif user_choice == 'P' and computer_choice == "Rock":
    print("You win")
elif user_choice == 'P' and computer_choice == "Scissors":
    print("You lose")
elif user_choice == 'S' and computer_choice == "scissors":
    print("Draw")
elif user_choice == 'S' and computer_choice == "Rock":
    print("You lose")
elif user_choice == 'S' and computer_choice == "Paper":
    print("You won")
#end if


