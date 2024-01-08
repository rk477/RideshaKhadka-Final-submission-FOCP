# 4. Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way.

# Program to encrypt a message by removing spaces and reversing the string

def encrypt_message(message_to_encrypt):
    # Remove spaces from the message
    message_without_spaces = message_to_encrypt.replace(" ", "")
    
    # Reverse the string
    encrypted_message = message_without_spaces[::-1]
    
    return encrypted_message

# Example usage and display output
user_input_message = input("Enter a message: ")
encrypted_output = encrypt_message(user_input_message)
print(f"The encrypted message is: {encrypted_output}")

