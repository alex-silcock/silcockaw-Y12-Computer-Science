sixletter_word = input("Enter a six-letter word ")

if len(sixletter_word) > 6 or len(sixletter_word) < 6:
    print("Your word is not 6 letters")
#end if

print(sixletter_word [::-1])