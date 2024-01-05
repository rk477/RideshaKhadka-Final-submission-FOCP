# 4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.


# Program to distribute sweets among pupils
total_sweets_count = int(input("Enter the total number of sweets: "))
num_of_pupils = int(input("Enter the number of pupils: "))

# Calculating sweets per pupil and left-over sweets
sweets_per_pupil = total_sweets_count // num_of_pupils
remaining_sweets = total_sweets_count % num_of_pupils

# Fixing grammar in the output
remaining_sweets_word = "sweets" if remaining_sweets > 1 else "sweet"

# Displaying output
print(f"Each pupil will receive {sweets_per_pupil} sweets and there will be {remaining_sweets} {remaining_sweets_word} left over.")
