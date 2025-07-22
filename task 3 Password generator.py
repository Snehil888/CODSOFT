import random
import string

print("Welcome to the Password Generator!")

try:
    length = int(input("Give the lenght of the password : "))

    if length < 4:
        print("Password length should be at least 4 characters for security reasons.")
    else:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for _ in range(length))
        print("\nHere is your secure password:")
        print(password)
except ValueError:
    print("Please enter a valid number.")

