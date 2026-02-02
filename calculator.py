#functions
#function for addition operation
def addition(a, b):
    return a + b
#function for subtraction operation
def subtraction(a, b):
    return a - b
#function for multiplication operation
def multiplication(a, b):
    return a * b
#function for division operation
#used conditional statement to handle zero division error 
def division(a, b):
    if b == 0:
        return "Division by zero is not valid,try with non zero number:"
    else:
        return a / b
        
#while loop for menu selection 
while True:
    menu = print("""===========================\nCalculator Application\n===========================\nSelect Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit""")
    try:
        value = int(input("select a value from given menu:"))
    except ValueError:
        print("Error: Invalid option. Please select a number between 1 and 5")
        continue    
    #if-else conditional statement for variable input.
    #try-except for handling variable input exceptions.     
    if value in [1,2,3,4]:
        try:
            a = float(input("Enter a value:"))
            b = float(input("Enter b value:"))
        except ValueError:
            print("invalid input!,enter a numeric value.")
            continue

    #nested if-else statements to  call suitable function for selected operation from given menu.     
    if value == 1:
        print("Result:", addition(a, b))
    elif value == 2:
        print("Result:", subtraction(a, b))
    elif value == 3:
        print("Result:", multiplication(a, b))
    elif value == 4:
        print("Result:", division(a, b))
    elif value ==5:
        print("Thank you for using Calculator Application. Goodbye!")
        break    
    else:
        print("Error: Invalid option. Please select a number between 1 and 5")
