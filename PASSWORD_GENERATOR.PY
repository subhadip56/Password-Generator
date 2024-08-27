import random
import string

print('Welcome to the Password Generator!')

letters = string.ascii_letters  # All uppercase and lowercase letters
symbols = string.punctuation  # All punctuation symbols
digits = string.digits  # All digits 0-9
allChar = letters + symbols + digits  # Combine all characters

# Get the number of letters, symbols, and digits for the password
letterNo = int(input('How many letters would you like in your password?\n'))
symbolNo = int(input('How many symbols would you like?\n'))
digitNo = int(input('How many digits would you like?\n'))
TotalNo = letterNo + symbolNo + digitNo  # Total number of characters in the password

# Generate the password
for i in range(TotalNo):
    print(random.choice(allChar), end="")  # Randomly choose and print each character
