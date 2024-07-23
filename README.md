
```markdown
# Student Grades Management System

## Overview

This Python script provides a simple console-based system for managing student grades. It allows users to perform the following operations:

- Enter new grades for existing students.
- Remove students from the system.
- Calculate and display the average grade for each student.
- Basic user authentication to access the system.

## Features

1. **Enter Grades**: Add grades to an existing student's record.
2. **Remove Student**: Remove a student's record from the system.
3. **Student Average Grades**: Calculate and display the average grade for each student.
4. **User Authentication**: Basic login mechanism to authenticate users before accessing the system.

## Code Structure

### Variables

- `admin`: Dictionary storing usernames and passwords for authentication.
- `studentInfo`: Dictionary storing student names and their associated grades.

### Functions

1. **`enterGrades()`**: Prompts for a student's name and grade, then adds the grade to the student's record if the student exists.
2. **`removeStudent()`**: Prompts for a student's name to remove their record from the system if the student exists.
3. **`studentAvgGrade()`**: Calculates and prints the average grade for each student in the `studentInfo` dictionary.
4. **`main()`**: Displays the menu and handles user input to call the appropriate function based on the user's choice.

### Main Execution

- The script starts by prompting for a username and password.
- If authentication is successful, it enters a loop to continuously display the menu and handle user choices.
- If the username or password is incorrect, it displays an error message and exits.

## Usage

1. **Run the Script**:
   ```bash
   python script.py
   ```

2. **Login**:
   - Enter the username and password as prompted. The default admin credentials are:
     - Username: `Pavankushana`
     - Password: `Pavan_1919`

3. **Menu Options**:
   - **Enter Grades**: Add a grade to an existing student's record.
   - **Remove Student**: Remove a student's record from the system.
   - **Student Average Grades**: Display the average grade for each student.
   - **Exit**: Exit the program.

## Example

Here's an example of how the script might look during execution:

```
Username: Pavankushana
Password: Pavan_1919
Welcome, Pavankushana

    Welcome to Grade Central
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    
What would you like to do Today? (Enter a number  ) 1
Enter Student Name: Jay
Enter Student Grade: 92
Adding Grade...
{'Jay': [67, 78, 85, '92'], 'Omsai': [78, 89, 90], 'Ranjith': [66, 77, 88]}

    Welcome to Grade Central
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    
What would you like to do Today? (Enter a number  ) 3
Jay has an Average of : 82.5
Omsai has an Average of : 85.66666666666667
Ranjith has an Average of : 77.0
```

## Notes

- Ensure to replace `script.py` with the actual filename of your Python script.
- The script uses `mean` from the `statistics` module to calculate the average grades.
- The script will exit if an invalid option is selected or upon choosing the exit option.
