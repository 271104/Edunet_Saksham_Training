# password = input("Enter Password: ")
# a = len(password)
# if ( a > 8 and a < 16 and password.isalnum()):
#         print("Valid Password")
# else:
#         print("Invalid Password")

import re

password = input("Enter Password: ")
a = len(password)

# Checking conditions
if (8 <= a <= 16 and
    password[0].isupper() and
    re.search(r'[A-Za-z]', password) and  # At least one alphabet
    re.search(r'\d', password) and        # At least one digit
    re.search(r'[^A-Za-z0-9]', password)  # At least one special character
   ):
    print("Valid Password")
else:
    print("Invalid Password")

# Exlpanation
# Used the re module (Regular Expressions) to check:
# [A-Za-z] → Ensures the password has at least one alphabet.
# \d → Ensures the password has at least one numeric digit.
# [^A-Za-z0-9] → Ensures the password has at least one special character.
# Combined all conditions using and to ensure all are met.
# Retained print(dir(password)) if you want to see available string methods (not necessary for password validation).
