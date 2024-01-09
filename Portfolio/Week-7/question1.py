# 1. Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


# Program to return a sorted list of unique letters in a string

def unique_letters(input_str):
    # Use set to remove duplicates, then convert it to a list
    letters_list = list(set(input_str))
    
    # Sort the list
    sorted_unique_letters = sorted(letters_list)
    
    return sorted_unique_letters

# Get user input
user_input = input("Enter a string: ")

# Function call
result = unique_letters(user_input)

# Display output
print(f"Unique letters in '{user_input}': {result}")

