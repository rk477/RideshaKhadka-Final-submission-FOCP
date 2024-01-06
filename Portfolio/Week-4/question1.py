# 1. Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.


# Function to validate if an integer is in the range 0 to 100 (inclusive)
def is_valid_integer(number):
    # Check if the number is within the specified range
    return 0 <= number <= 100

def main():
    # Get user input
    user_input = int(input("Enter an integer: "))

    # Validate the entered integer using the is_valid_integer function
    validation_result = is_valid_integer(user_input)

    # Display the result based on the validation
    if validation_result:
        print("The entered integer is in the range 0 to 100 (inclusive).")
    else:
        print("The entered integer is outside the valid range.")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

