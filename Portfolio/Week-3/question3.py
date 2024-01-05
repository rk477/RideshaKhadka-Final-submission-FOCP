# 3. Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

# Program to simulate user password input with length check
password_1 = input("Enter a new password (8-12 characters): ")
password_2 = input("Enter the password again: ")

# Checking if the passwords meet the length requirement and match
if (8 <= len(password_1) <= 12) and (8 <= len(password_2) <= 12) and (password_1 == password_2):
    print("Password set successfully!")
else:
    print("Passwords do not meet the length requirement or do not match. Please try again.")

