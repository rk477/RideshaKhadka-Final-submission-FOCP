# . Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

# Program to simulate user password input
user_password_1 = input("Enter a new password: ")
user_password_2 = input("Enter the password again: ")

# Checking if the passwords match
if user_password_1 == user_password_2:
    print("Password set successfully!")
else:
    print("Passwords do not match. Please try again.")

