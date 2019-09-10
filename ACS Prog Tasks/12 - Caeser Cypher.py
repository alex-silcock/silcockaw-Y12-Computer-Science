user_input = input("Enter word ")
ascii_input = ord(user_input)

cypher_list = []

new_ascii_input = ascii_input + 2
cypher_list.append(chr(new_ascii_input))

print(cypher_list)

