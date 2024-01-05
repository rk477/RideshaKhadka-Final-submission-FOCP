# 1. Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

# Program to greet the user by their name or as Stranger
user_input_name = input("Hello, what is your name? ")

# Displaying output
if not user_input_name:
    print("Hello, Stranger!")
else:
    print(f"Hello, Mr/Ms {user_input_name}. Good to meet you!")
