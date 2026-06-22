# Import Pandas library
import pandas as pd

# Import Matplotlib library for charts
import matplotlib.pyplot as plt

# Display application title
print("--- Student Attendance Management ---")

print("-----------------------------------")

# Create an empty DataFrame to store student records
task = pd.DataFrame(columns=['Name', 'Age', 'Class', 'Attendance'])

# Main program loop
while True:

    # Display menu options
    print("1. Add Student")
    print("2. View Student")
    print("3. Remove Student")
    print("4. Student Attendance Report")
    print("5. Exit")
    print("-----------------------------------")

    # Get user choice
    userchoice = int(input("Enter the option : "))

    # Add Student
    if (userchoice == 1):

        # Loop to add multiple students
        while True:
            print("-----------------------------------")

            # Take student details as input
            name = input("Enter the Student Name : ")
            age = int(input("Enter the age of Student : "))
            classes = int(input("Enter the classes of Student : "))
            attendance = int(input("Enter the attendance of Student : "))

            # Add student data to DataFrame
            task.loc[len(task)] = [name , age , classes , attendance]

            # Display current student records
            print(task.to_string(index = False))
            print("-----------------------------------")

            # Ask user whether to add another student
            choice = input("Add another Student? (y/n): ")

            # Save data and exit Add Student loop
            if choice.lower() == 'n':

                # Save student data to CSV file
                task.to_csv("Students.csv")
                break

            print("-----------------------------------")

    # View Student Records
    elif (userchoice == 2):

        try:

            # Ask for file name or location
            file = input("Enter the file name Or location : ")

            # Read student data from CSV file
            task = pd.read_csv("Students.csv")

            # Display all student records
            print(task.to_string(index=False))

        # Handle file not found or other errors
        except:
            print("Student Not Found")

    # Remove Student
    elif (userchoice == 3):

        # Ask for student name to remove
        name = input("Enter the EMP Name : ")

        # Read student data from CSV
        task = pd.read_csv("Students.csv")

        # Remove matching student records
        task = task.drop(task[task.Name == name].index)

        # Save updated data back to CSV
        task.to_csv("Students.csv", index=False)

        print("-----------------------------------")

        # Display updated student list
        print(task.to_string(index=False))

    # Student Attendance Report
    elif (userchoice == 4):

        # Loop to add attendance data and generate report
        while True:
            print("-----------------------------------")

            # Take student details as input
            name = input("Enter the Student Name : ")
            age = int(input("Enter the age of Student : "))
            classes = int(input("Enter the classes of Student : "))
            attendance = int(input("Enter the attendance of Student : "))

            # Add student data to DataFrame
            task.loc[len(task)] = [name , age , classes , attendance]

            # Display current records
            print(task.to_string(index = False))
            print("-----------------------------------")

            # Ask user whether to add another student
            choice = input("Add another Student? (y/n): ")

            # Save data and generate report
            if choice.lower() == 'n':

                # Save student data to CSV
                task.to_csv("Students.csv")

                try:

                    # Ask for file name or location
                    file = input("Enter the file name Or location : ")

                    # Read data from CSV file
                    task = pd.read_csv("Students.csv")

                    # Create attendance bar chart
                    plt.bar(task['Name'] , task['Attendance'])

                    # Add chart title and labels
                    plt.title("Student Attendance Report")
                    plt.xlabel("Student Name")
                    plt.ylabel("Attendance")

                    # Save chart as image file
                    plt.savefig("student_rep.png")

                    # Display chart
                    plt.show()

                    break

                # Handle file reading errors
                except:
                    print("No Student Data Found")

            print("-----------------------------------")

    # Exit program
    elif (userchoice == 5):
        break

    # Handle invalid menu option
    else:
        print("-----------------------------------")
        print("Invalid option")
        print("-----------------------------------")