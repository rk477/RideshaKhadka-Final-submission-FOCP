# 7. Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.

# Program to display the customized times table
user_selected_table = int(input("Enter the number for times table (0-12): "))

if 0 <= user_selected_table <= 12:
    for factor in range(13):
        product = factor * user_selected_table
        print(f"{factor} x {user_selected_table} = {product}")
else:
    print("Error: Please enter a number between 0 and 12.")
