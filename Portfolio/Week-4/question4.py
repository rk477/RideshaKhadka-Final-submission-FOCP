# 4. When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)


# Function to remove the last character from a string
def remove_last_character(input_str):
    # Checking if the string has one or fewer characters
    if len(input_str) <= 1:
        return input_str

    # Remove the last character
    return input_str[:-1]

# Testing the function
user_input_str = input("Enter a string: ")
result_str = remove_last_character(user_input_str)

print(f"Original string: {user_input_str}")
print(f"String with the last character removed: {result_str}")

