# 8. Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".


# Program to display the customized times table (backward if negative)
selected_table = int(input("Enter the number for times table (-12 to 12): "))

if -12 <= selected_table < 0:
    for multiplier in range(12, -1, -1):
        result = multiplier * selected_table
        print(f"{multiplier} x {selected_table} = {result}")

elif 0 <= selected_table <= 12:
    for multiplier in range(13):
        result = multiplier * selected_table
        print(f"{multiplier} x {selected_table} = {result}")
else:
    print("Error: Please enter a number between -12 and 12.")


