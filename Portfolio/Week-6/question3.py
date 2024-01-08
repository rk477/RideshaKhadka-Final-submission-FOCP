# 3. Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.


# Program to check if a given integer is a prime number

def is_prime(number_to_check):
    if number_to_check <= 1:
        return False
    for i in range(2, int(number_to_check**0.5) + 1):
        if number_to_check % i == 0:
            return False
    return True

# Example usage and display output
user_input_number = int(input("Enter an integer: "))
if is_prime(user_input_number):
    print(f"{user_input_number} is a prime number.")
else:
    print(f"{user_input_number} is not a prime number.")


