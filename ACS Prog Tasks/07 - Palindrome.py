sixletter_word = input("Enter a six-letter word ")

while len(sixletter_word) > 6 or len(sixletter_word) < 6:
    print("Your word is not 6 letters")
    sixletter_word = input("Enter a six-letter word ")
#end while

print(sixletter_word [::-1])

