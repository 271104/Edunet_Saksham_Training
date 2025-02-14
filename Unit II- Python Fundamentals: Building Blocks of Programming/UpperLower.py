word = input("Enter any word: ")
new_word = ""

for char in word:
    if char.isupper():
        new_word += char.lower()
    elif char.islower():
        new_word += char.upper()
    else:
        new_word += char  

print(new_word)
