📊 Data Analyzer and Transformer Program

A simple Python-based Data Analyzer and Transformer that allows users to input numerical data and perform various operations such as calculating statistics, factorials, filtering, and sorting.

This project demonstrates the use of Python built-in functions, recursion, lambda functions, filter(), sorted(), lists, functions, and loops.

🚀 Features

The program provides the following operations:

Input Data

Accepts a 1D array of integers from the user.
Stores the entered values in a Python list.

Display Data Summary

Displays the total number of elements.
Finds the minimum value.
Finds the maximum value.
Calculates the sum.
Calculates the average.

Calculate Factorial

Calculates the factorial of a number.
Uses recursion to perform the calculation.

Filter Data by Threshold

Filters values based on a user-defined threshold.
Uses a lambda function with Python's filter() function.

Sort Data

Sorts the entered data in:
Ascending order
Descending order
Uses Python's built-in sorted() function.

Display Dataset Statistics

Displays minimum value.
Displays maximum value.
Displays total sum.
Displays average value.

Exit Program

Safely exits the program.
🛠️ Technologies Used
Python 3
Python Lists
Functions
Recursion
Lambda Functions
filter()
sorted()
Built-in functions:
len()
min()
max()
sum()
📋 Main Menu

When the program starts, the following menu is displayed:

Welcome to the Data Analyzer and Transformer Program

Main Menu :
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial Recursion
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

▶️ How to Run
1. Install Python

Make sure Python 3 is installed on your system.

You can check your Python version using:

python --version


or:

python3 --version

2. Save the Program

Save the Python source code as:

data_analyzer.py

3. Run the Program

Open a terminal in the project directory and run:

python data_analyzer.py

💻 Example Usage
Input Data
Please enter your choice : 1

Enter data for a 1D array (separated by spaces) : 10 25 5 40 15 30
Data has been stored Successfully !

Display Data Summary
Please enter your choice : 2

- Data Summary :-
- Total elements :  6
- Minimum value :  5
- Maximum value :  40
- Sum of all values :  125
- Average value :  20.833333333333332

Calculate Factorial
Please enter your choice : 3

Enter a number to calculate its factorial : 5
Factorial of  5 is :  120

Filter Data
Please enter your choice : 4

Enter a threshold value to filter out data above this value : 20
Filtered Data (values >= 20) :
[25, 40, 30]

Sort Data
Ascending
Choose sorting option :
1. Ascending
2. Descending

Enter your choice : 1

Sorted data in Ascending Order :
[5, 10, 15, 25, 30, 40]

Descending
Sorted data in Descending Order :
[40, 30, 25, 15, 10, 5]

📂 Project Structure
Data-Analyzer-and-Transformer/
│
├── data_analyzer.py
└── README.md

🧠 Concepts Demonstrated
Functions

The program uses separate functions for different operations:

def Display_Data_Summary(a):
    ...

def factorial(num):
    ...

def Dataset_Statistics(a):
    ...


This makes the program easier to understand and maintain.

Recursion

The factorial function uses recursion:

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


For example:

5! = 5 × 4 × 3 × 2 × 1 = 120

Lambda Function and Filter

The filtering operation uses:

filter(lambda x: x >= y, a)


This returns values that are greater than or equal to the specified threshold.

Sorting

The program uses Python's built-in sorted() function:

sorted(a, reverse=False)


for ascending order and:

sorted(a, reverse=True)


for descending order.

⚠️ Important Notes
Data should be entered as integers separated by spaces.
Options such as Summary, Filtering, Sorting, and Statistics require data to be entered first using Option 1.
The factorial input should be a non-negative integer.
The program continues running until the user selects Option 7.
🔧 Possible Improvements

The project can be improved further by adding:

Input validation and error handling.
Prevention of operations before data is entered.
Support for decimal/float values.
A function to clear or reset the dataset.
More statistical calculations such as:
Median
Mode
Standard deviation
Saving and loading datasets from files.
A graphical user interface (GUI).
Returning statistics as multiple values instead of only printing them.
👨‍💻 Learning Objectives

This project is useful for learning and practicing:

Python programming fundamentals
Lists and arrays
User input
Conditional statements
Loops
Functions
Recursion
Lambda functions
Filtering
Sorting
Built-in Python functions
Basic data analysis
📜 License

This project is created for educational and learning purposes.

⭐ Author
DHRUV RAO

Thank you for checking out the Data Analyzer and Transformer Program! 🚀
