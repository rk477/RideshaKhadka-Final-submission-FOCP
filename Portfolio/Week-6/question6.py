# 6. Write a program that decrypts messages encoded as above.

# Program to decrypt messages encoded with random intervals

import random
import string

def encrypt_message():
    # Ask the user for a message
    user_message = input("Please enter a message: ")

    # Generate a random interval between 2 and 20
    random_interval = random.randint(2, 20)

    # Initialize the encrypted message
    encrypted_message = ""

    # Iterate over each character in the message
    for char in user_message:
        # If the character is a space, add it to the encrypted message
        if char == " ":
            encrypted_message += char
        else:
            # Add the character and fill the gaps with random letters
            encrypted_message += char + ''.join(random.choice(string.ascii_lowercase) for _ in range(random_interval))

    print(f"Original message: {user_message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Interval used: {random_interval}")

def decrypt_message():
    # Ask the user for the encrypted message and the interval used
    encrypted_message = input("Please enter the encrypted message: ")
    interval = int(input("Please enter the interval used: "))

    # Initialize the decrypted message
    decrypted_message = ""

    # Iterate over each character in the encrypted message
    for i in range(0, len(encrypted_message), interval+1):
        # Add the character to the decrypted message
        decrypted_message += encrypted_message[i]

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

# Call the functions
encrypt_message()
decrypt_message()
