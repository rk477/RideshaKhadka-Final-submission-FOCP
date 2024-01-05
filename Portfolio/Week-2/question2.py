# 2. Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.


# Program to convert Celsius to Fahrenheit
user_input_celsius = float(input("Enter a temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit_temperature = (9/5) * user_input_celsius + 32

# Displaying output
print(f"{user_input_celsius}C is equivalent to {fahrenheit_temperature}F.")
