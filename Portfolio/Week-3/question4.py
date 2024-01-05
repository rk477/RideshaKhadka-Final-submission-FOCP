# 4. Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


# Program to simulate user password input with length and common password check
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Get user input
user_password_1 = input("Enter a new password (8-12 characters): ")
user_password_2 = input("Enter the password again: ")

# Check conditions for password set
if (8 <= len(user_password_1) <= 12) and (8 <= len(user_password_2) <= 12) and (user_password_1 not in BAD_PASSWORDS) and (user_password_1 == user_password_2):
    print("Password set successfully!")
else:
    print("Password does not meet the constraints or it is a common password. Please try again.")
