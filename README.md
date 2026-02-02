# Calculator Application – Python
A simple command-line calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. This project follows the structure and requirements defined in the Software Requirements Document, including input validation, error handling, and a menu-driven user interface.

## How to Run the Application
1. Requirements:
Python 3 installed on your system

2. Steps to Run:
Download or clone the repository 
git clone <https://github.com/RANGAHARISH/Calculator.git>

3. Open the folder in your terminal.
Run the Python file:python calculator.py

4. The calculator menu will appear.
Choose an option (1–5) and follow the instructions.

## Sample Inputs and Outputs

```
Sample Run 1 (Addition):
=============================
Calculator Application
=============================
Select Operation
1: Addition
2: Subtraction
3: Multiplication
4: Division
5: Exit

Select a value: 1
Enter a value: 10
Enter b value: 20

Result: 30.0
```


```
Sample Run 2 (Division by Zero):
Select a value: 4
Enter a value: 20
Enter b value: 0
Error: Division by zero is not allowed. Please enter a non-zero number.
```

```
Sample Run 3 (Invalid Menu Input):
Select a value: 8
Error: Invalid option. Please select a number between 1 and 5.
```
```
Sample Run 4 (Exit):
Select a value: 5
Thank you for using Calculator Application. Goodbye!
```
## Design Decisions
1. Modular Functions
Each arithmetic operation is implemented as its own function:
addition(a, b)
subtraction(a, b)
multiplication(a, b)
division(a, b)
This keeps the code clean, reusable, and easy to test.

2. While Loop for Continuous Operation
A while True loop is used so the user can perform multiple calculations without restarting the program.

3. Input Validation
try-except blocks ensure:
Only numbers are accepted
Invalid menu choices do not crash the program

4. SRD Compliance
The program follows the SRD guidelines:
Menu formatting
Error messages
Division by zero handling
Validation for all inputs
Clear, user-friendly output

5. Easy Extensibility
The structure allows adding more operations in the future (square root, percentage, power).






