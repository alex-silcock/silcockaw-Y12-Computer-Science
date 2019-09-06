count = 5
max = 0
list1 = []   #list of the input word to be guessed
list_start=[]
list2 = []  #every letter guessed by the user

hangman_word = input("Player 1: Enter a word ")

length_word = len(hangman_word)

#print("Word to guess:", "*" * length_word)

for x in hangman_word:
    list1.append(x)

for x in range (length_word):
    list_start.append("*")


while count > 0:

    user_guess = input("Enter guess - You have " + str(count) + " lives left ")

    if user_guess in list1:
        print("letter is in word")
        index_user_guess = list1.index(user_guess)
        list_start[index_user_guess]=user_guess
        print(index_user_guess)
        list2.append(user_guess)
    else:
        count -= 1
    print(list2)
    print(list_start)










