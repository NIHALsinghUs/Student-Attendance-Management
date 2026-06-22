# Student Attendance Management System

## Overview

The Student Attendance Management System is a Python-based console application designed to help manage student records and attendance data efficiently. This project uses the Pandas library for data management and Matplotlib for data visualization. It provides a simple and user-friendly interface that allows users to add, view, remove, and analyze student attendance records.

The application stores student information in a CSV file, making data persistent even after the program is closed. It also generates attendance reports in the form of bar charts and saves them as image files for future reference.

This project is ideal for beginners who want to learn Python programming concepts such as file handling, data manipulation, exception handling, loops, conditional statements, and data visualization.

---

## Features

### Add Student Records

Users can add student details including:

* Student Name
* Age
* Class
* Attendance Percentage

The entered information is stored in a Pandas DataFrame and can be saved to a CSV file.

### View Student Records

The system can read student data from a CSV file and display all available records in a structured tabular format.

### Remove Student Records

Users can remove student records by entering the student's name. The selected record is deleted from the CSV file and the updated data is saved automatically.

### Attendance Report Generation

The application generates attendance reports using Matplotlib. Attendance data is displayed in the form of a bar chart, making it easier to compare attendance percentages among students.

### Report Export

Attendance charts can be saved as image files (PNG format) for documentation and reporting purposes.

### CSV Data Storage

All student records are stored in a CSV file, allowing data persistence and easy access without requiring a database.

---

## Technologies Used

### Python

The primary programming language used for developing the application.

### Pandas

Used for:

* DataFrame creation and management
* CSV file reading and writing
* Data manipulation and filtering

### Matplotlib

Used for:

* Creating attendance reports
* Visualizing attendance data using bar charts
* Exporting reports as image files

---

## Project Structure

```text
Student_Attendance_Management/
│
├── main.py
├── Students.csv
├── student_rep.png
├── README.md
│
└── requirements.txt
```

### File Description

#### main.py

Contains the complete source code of the Student Attendance Management System.

#### Students.csv

Stores all student records including names, age, class, and attendance details.

#### student_rep.png

Generated attendance report image created using Matplotlib.

#### README.md

Project documentation and usage guide.

#### requirements.txt

Contains project dependencies.

---

## Menu Options

When the application starts, users are presented with the following menu:

```text
1. Add Student
2. View Student
3. Remove Student
4. Student Attendance Report
5. Exit
```

### Option 1: Add Student

Allows users to add one or more student records.

### Option 2: View Student

Displays all saved student records from the CSV file.

### Option 3: Remove Student

Deletes a student record based on the entered student name.

### Option 4: Student Attendance Report

Generates a graphical attendance report using stored student data.

### Option 5: Exit

Closes the application.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/student-attendance-management.git
```

### Navigate to Project Directory

```bash
cd student-attendance-management
```

### Install Required Libraries

```bash
pip install pandas matplotlib
```

Or use:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Execute the following command:

```bash
python main.py
```

The menu-driven interface will appear in the terminal.

---

## Sample Data

```text
Name      Age    Class    Attendance
------------------------------------
Raj       18      12         90
Aman      17      11         85
Rohit     18      12         95
```

---

## Sample Attendance Report

The generated report displays student names on the X-axis and attendance percentages on the Y-axis.

Example:

```text
Attendance (%)
|
|         █
|     █   █
| █   █   █
|________________
  Raj Aman Rohit
```

The chart is automatically saved as:

```text
student_rep.png
```

---

## Learning Outcomes

This project helps learners understand:

* Python fundamentals
* Loops and conditional statements
* Exception handling
* File handling using CSV files
* Data manipulation with Pandas
* Data visualization using Matplotlib
* CRUD operations (Create, Read, Update, Delete)
* Project structure and documentation

---

## Future Enhancements

Potential improvements include:

* Student ID generation
* Search student functionality
* Update student records
* Attendance percentage validation
* Pie chart and line chart reports
* GUI using Tkinter
* Database integration using SQLite or MySQL
* User authentication system
* Export reports to PDF format
* Dashboard with multiple analytics charts

---

## Requirements

```text
Python 3.x
Pandas
Matplotlib
```

## Install dependencies:

```bash
pip install pandas matplotlib
```

---

## Conclusion

The Student Attendance Management System is a beginner-friendly Python project that demonstrates the integration of data management and visualization tools. By combining Pandas and Matplotlib, the application provides an efficient way to maintain student attendance records and generate meaningful reports. This project serves as an excellent learning resource for students and developers looking to strengthen their Python programming skills and gain practical experience with real-world data handling tasks.
