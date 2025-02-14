string = input("Enter the string:")
char = input("Enter the character to count:")
counter = 0
for c in string:
    if c == char:
        counter += 1
print("The character", char,"appears", counter, "times in the string.")
