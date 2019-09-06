
count = 1

#take input from player 1

hangman_word = input("Player 1: Enter a word ")
length_word = len(hangman_word)
print("Word to guess:", "*" * length_word)
hangman_word.split(hangman_word)

for count in range(1,5):
    p2_char_guess = input("You have " +str(count) + " guesses left - Letter?")
    
