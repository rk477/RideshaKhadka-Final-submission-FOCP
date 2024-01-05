# 5. Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.

# Program to simulate user password input with loop for retries
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    # Get user input
    user_password_1 = input("Enter a new password (8-12 characters): ")
    user_password_2 = input("Enter the password again: ")

    # Check conditions for password set
    if (8 <= len(user_password_1) <= 12) and (8 <= len(user_password_2) <= 12) and (user_password_1 not in BAD_PASSWORDS) and (user_password_1 == user_password_2):
        print("Password set successfully!")
        break
    else:
        print("Password does not meet the constraints or it is a common password. Please try again.")
