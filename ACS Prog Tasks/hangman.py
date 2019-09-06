count = 5
max = 0
list_word2b_guessed = []   #list of the input word to be guessed
list_start=[]
list_guesses = []  #every letter guessed by the user2

hangman_word = input("Player 1: Enter a word ")

length_word = len(hangman_word)

#print("Word to guess:", "*" * length_word)

for x in hangman_word:
    list_word2b_guessed.append(x)

for x in range (length_word):
    list_start.append("*")

#double-letters: loop through list and if it exists more than once then output it however many times in the new list

while count > 0:

    user_guess = input("Enter guess - You have " + str(count) + " lives left ")

    if user_guess in list_word2b_guessed:
        print("Letter is in word")
        index_user_guess = list_word2b_guessed.index(user_guess)
        list_start[index_user_guess] = user_guess
        #print(index_user_guess)
        if user_guess in list_guesses:
            print("You've already guessed the letter " + user_guess)
        else:
            list_guesses.append(user_guess)
            print(list_guesses)
            print(list_start)
    else:
        count -= 1
  











