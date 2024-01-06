# 3. Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.



# Getting user input and formatting it to capitalize the name
user_input_name = input("Hello, what is your name? ").capitalize()

# Displaying output
if not user_input_name:
    print("Hello, Stranger!")
else:
    print(f"Hello, Mr/Ms {user_input_name}. Good to meet you!")

