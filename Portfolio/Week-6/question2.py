# 2. Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).

# Program to find factors of an integer

def find_factors(integer_input):
    factors_list = []
    for i in range(1, integer_input + 1):
        if integer_input % i == 0:
            factors_list.append(i)
    return factors_list

# Example usage and display output
user_number = int(input("Enter an integer: "))
resulting_factors = find_factors(user_number)
print(f"The factors of {user_number} are: {resulting_factors}")

