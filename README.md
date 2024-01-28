## Programming Portfolio for Computer Programming Module

### Project Overview:
Welcome to my Programming Portfolio repository for the Computer Programming module at Leeds Beckett University. This repository showcases my journey through the module, demonstrating my understanding of key programming concepts and skills.
In this portfolio, you'll find a collection of weekly tasks, programming solutions, and additional programs developed during the course. Each section is organized meticulously to provide a structured overview of my progress and proficiency in Python programming.
The repository contains weekly tasks and programming tasks (Task1, Task2, Task3). The README will be regularly updated to reflect my latest achievements and completed tasks, providing a comprehensive record of my learning journey.

### Repository Structure

- **Portfolio**: Contains weekly task folders for each week.

  -	**Week 1**: The week 1 tasks include studying Exercises01.pdf and solutions of five programming problems in Programs 01.

  -	**Week 2**: The week 2 tasks contain Exercises02.pdf, Practical02.pdf, and solutions of four programming challenges in Programs 02 for this week.

  -	**Week 3**: The week 3 tasks contain Exercises03.pdf, Practical03.pdf, and solutions of eight programming tasks in Programs 03 during this week.

  -	**Week 4**: The week 4 tasks contain Exercises04.pdf, Practical04.pdf, and solutions of eight programming challenges in Programs 04 as part of this week's assignments.

  -	**Week 5**: The week 5 tasks involve Exercises05.pdf and solutions for three programming problems in Programs 05. Additionally, work with demofile.txt and its backup for extra tasks.

  -	**Week 6**: The week 6 tasks contain Exercises06.pdf, Practical06.pdf, and solutions to six programming problems in Programs 06 during this week.

  -	**Week 7**: The week 7 tasks contain Exercises07.pdf, Practical07.pdf, and solutions of four programming challenges in Programs 07 as part of this week's agenda.

  -	**Week 8**: The week 8 tasks contain Exercises08.pdf and solutions of five programming tasks in Programs 08. Additionally, work with demofile.txt and include the dictionary file - words_alpha.txt.


**Task 1**: Folder containing a Python script named `Task1.py`.

  -  It calculates pizza orders including discounts based on user input (delivery required?, is it Tuesday, Did the customer use the app?) and returns the total price of the pizza ordered.

**Task 2**: Folder containing a Python script named `Task2.py` and 3 additional `shelter.log` files.

  - It analyzes `shelter.log` files and calculates and returns values such as `our_cat_visits`, `other_cats_visits`, `our cat's total time in the shelter`, `average visit of our cat`, `shortest and longest visit of our cat` using the `sys` module to access command line arguments and displays result if no command line arguments were provided; otherwise, throws an error saying: "missing command line arguments."

**Task 3**: Folder containing a Python script named `Task3.py` and one `passwd.txt` file.  It contains 6 functions:
  
  - **`encrypt(text)`:** ROT13 encryption.

  - **`add_user`:** Adds a new user to the password file.
  
  - **`delete_user()`:**  Deletes a user from the password file.

  - **`change_password`:** Changes the password for a user in the password file.

  - **`login`:** Checks if a user can log in with the provided username and password.
    
  - **`main`:** Calls the main function.

### Task Details

#### Task 1: Pizza Order Calculator  (Task1.py)

**Description**:

• It calculates the total price of a pizza order, considering discounts based on user inputs (delivery requirements, day of the week, app usage).

**Functions**:

  - **`get_user_input(get_input)`:** Ensures valid positive integer input from the user.

  - **`get_yes_or_no(get_str)`:** Gets valid yes or no input from the user.

  - **`calculate_order_price(total_pizzas, tuesday_offer, delivery_required, bpp_app_use)`:** Calculates and returns the total price of the pizza order.

  - **`display_total_price(total_price)`:** Displays the total price.

**Example Usage**:

```text
PS C:\Users\rides\OneDrive\Desktop\Task1> python -u "c:\Users\rides\OneDrive\Desktop\Task1\Task1.py"

BPP Pizza Price Calculator
==========================

How many pizzas ordered? 7
Is delivery required? y
Is it Tuesday? n
Did the customer use the app? y

Total Price: £63.00.
 ```

**Example Usage with Exception Handling**:

```text
PS C:\Users\rides\OneDrive\Desktop\Task1> python -u "c:\Users\rides\OneDrive\Desktop\Task1\Task1.py"

BPP Pizza Price Calculator
==========================

How many pizzas ordered? hello
Please enter a number!
How many pizzas ordered? 5
Is delivery required? 0-
Please answer 'Y' or 'N'.
Is delivery required? y
Is it Tuesday? no 
Please answer 'Y' or 'N'.
Is it Tuesday? y
Did the customer use the app? not used
Please answer 'Y' or 'N'.
Did the customer use the app? y

Total Price: £22.50.
```

#### Task 2: Shelter Log Analyzer (Task2.py)

**Description**:

• It analyzes a log file from a cat shelter, providing statistics on cat visits, total time spent, and visit durations.

**Functions**:

 -  **`analyze_shelter_logs(log_file_path)`:** Analyzes the specified log file and prints relevant statistics.
   
 -  **`main()`:** Calls the main function.

Note: Requires a command line argument specifying the log file path.

**Example Usage**:

```text
Log File Analysis
==================

Cat Visits: 12
Other Cats: 58

Total Time in house: 4 hours, 5 minutes

Average Visit Length: 20 minutes
Longest Visit:        45 minutes
Shortest Visit:       5 minutes

PS C:\Users\rides\OneDrive\Desktop\Task2> python task2.py shelter_2023-08-26.log

Log File Analysis
==================

Cat Visits: 11
Other Cats: 45

Total Time in house: 5 hours, 0 minutes

Average Visit Length: 27 minutes
Longest Visit:        45 minutes
Shortest Visit:       10 minutes

```

**Example Usage with Exception Handling**:

```text
PS C:\Users\rides\OneDrive\Desktop\Task2> python -u "c:\Users\rides\OneDrive\Desktop\Task2\Task2.py"
Missing command line arguements!
PS C:\Users\rides\OneDrive\Desktop\Task2> python task2.py shelter_2023-08-26    
Can't open'shelter_2023-08-26'!
PS C:\Users\rides\OneDrive\Desktop\Task2> python task2.py shelter_2023-08-25.log
Our cat visits not recorded in the log file.
```

#### Task 3: User Management System (Task3.py)

 **Description**:
 
• It manages user accounts with functionalities such as adding, deleting, changing passwords, and user login authentication.

**Functions**:

   -	**`encrypt(text)`:** ROT13 encryption.

   -  **`add_user()`:** Adds a new user to the password file.

   - 	**`delete_user()`:** Deletes a user from the password file.

   - 	**`change_password()`:** Changes the password for a user in the password file.

   - 	**`login()`:** Checks if a user can log in with the provided username and password.

   - **`main()`:** Calls the main function.

Note: Passwords are encoded using ROT13 before storing for basic security.

These scripts collectively demonstrate proficiency in user input handling, file operations, and basic user account management.

**Example Usage**:

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): adduser
Enter new username: ridesha
Enter real name: Ridesha Khadka
Enter password: rrrrrrr
User Created.
PS C:\Users\rides\OneDrive\Desktop\Task3> cat passwd.txt
rved:Robbie Veronica Edna Davis:gvevatzbfflinevnoyl
ridesha:Ridesha Khadka:eeeeeee
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): login
User: ridesha
Password:
Access granted.
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): passwd
User: ridesha
Current Password: 
New Password: 
Confirm: 
Password changed.
PS C:\Users\rides\OneDrive\Desktop\Task3> cat passwd.txt
rved:Robbie Veronica Edna Davis:gvevatzbfflinevnoyl
ridesha:Ridesha Khadka:uuuuuuu
 ```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): deluser
Enter username: ridesha
User Deleted.
PS C:\Users\rides\OneDrive\Desktop\Task3> cat passwd.txt
rved:Robbie Veronica Edna Davis:gvevatzbfflinevnoyl
 ```

**Example Usage with Exception Handling**:

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): adduser
Enter new username: ridesha
Username already exists. Cannot add user.
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): login
User: @ridesha
Password: 
Access denied.
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): passwd
User: ridesha
Current Password: 
Current password is incorrect.
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): passwd
User: ridesha
Current Password: 
New Password: 
Confirm: 
Passwords do not match. Nothing changed.
```

```text
PS C:\Users\rides\OneDrive\Desktop\Task3> python -u "c:\Users\rides\OneDrive\Desktop\Task3\Task3.py"
Enter command (adduser, deluser, passwd, login, quit): deluser
Enter username: ridesha
User not found.
 ```

### Issues Encountered and Solved:

**1.**	Understanding Requirements: 
I faced some difficulties comprehending the specifics of weekly tasks and exercises. However I got engaged actively with tasks, sought clarifications, and improved my understanding through hands-on application. I regularly checked the GitHub repository which ensured me alignment with requirements. 

**2.**	Efficient GitHub Use:
It was difficult at first to have an organized repository and use GitHub for version control. But as I spent time learning GitHub made regular commits, and adhered to a structured organization. It made it easier for me to keep track of the project's advancement. 

**3.**	Debugging and Resolving Errors:
Finding and fixing programming problems was a frequent challenge. However, I was able to increase code quality by using IDE tools, adopting a methodical debugging approach, and making code improvements based on error warnings.

**4.**	Using External Resources:
It took some skill to handle and add extra data when using external resources, like the dictionary "words_alpha.txt," in programming tasks.  Although it was a little difficult, this improved my learning process and helped me come up with workable answers.

### Language and Tools Used:
- **Programming Language**: Python 3.10.7
- **IDE/Text Editor**: Visual Studio Code (VSCode)/Windows PowerShell
  
### Contact Information
-	Email: kridesha22@tbc.edu.np
-	GitHub: https://github.com/rk477
  
 <p align="center">This README.md file serves as documentation for my programming portfolio.</p>
