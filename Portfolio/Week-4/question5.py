# 5. Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    return celsius_temp

def main():
    # Testing the functions
    user_input_celsius = float(input("Enter temperature in Celsius: "))
    result_fahrenheit = celsius_to_fahrenheit(user_input_celsius)
    print(f"{user_input_celsius} degrees Celsius is equal to {result_fahrenheit:.2f} degrees Fahrenheit.")

    user_input_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result_celsius = fahrenheit_to_celsius(user_input_fahrenheit)
    print(f"{user_input_fahrenheit} degrees Fahrenheit is equal to {result_celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()




