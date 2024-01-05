# 5. The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over" group.

# Program to calculate lab groups for a given number of students
student_counts = [113, 175, 12]
students_per_group = 24

for total_students in student_counts:
    # Calculate full groups and remaining students
    full_groups = total_students // students_per_group
    remaining_students = total_students % students_per_group
    
    # Displaying results
    print(f"For {total_students} students: Full groups: {full_groups}, Remaining students: {remaining_students}")
