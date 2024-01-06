# 2. Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def count_upper_lower(input_str):
    # Initialize counters
    upper_count = 0
    lower_count = 0

    # Count uppercase and lowercase letters
    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

def main():
    # Get user input
    user_input_str = input("Enter a string: ")

    # Call the function to count uppercase and lowercase letters
    result_upper, result_lower = count_upper_lower(user_input_str)

    # Display the results
    print(f"Number of Uppercase letters: {result_upper}")
    print(f"Number of Lowercase letters: {result_lower}")

if __name__ == "__main__":
    main()
