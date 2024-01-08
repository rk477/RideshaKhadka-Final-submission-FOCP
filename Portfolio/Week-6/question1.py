# 1. Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

# Program to convert a positive integer to binary representation

def get_positive_integer():
    num = int(input("Enter a positive integer: "))
    return num

def decimal_to_binary_representation(positive_integer):
    return bin(positive_integer)

def display_binary_representation(decimal_input, binary_representation):
    print(f"The binary representation of {decimal_input} is: {binary_representation}")

# Get input, convert to binary, and display the result
decimal_number_input = get_positive_integer()
binary_representation_output = decimal_to_binary_representation(decimal_number_input)
display_binary_representation(decimal_number_input, binary_representation_output)
