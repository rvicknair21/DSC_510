#File: Assignment_5_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: April 12, 2019
#Course: DSC 510
#Usage: Calculator

def performCalculation(operator):
    '''prompt the user to enter two numbers and perform a calculation.  print the calculated value'''
    x,y = input("Enter two numbers separated by a comma:\n").split(",")

    #check to make sure a number was entered by converting it to a float data type.
    #if a number is not entered, a while loop will continue to prompt the user until a number is entered
    try:
        x = float(x)
        y = float(y)
    except:
        error = True
        while error:
            x,y = input("Invalid Entry. Enter two numbers separated by a comma:\n").split(",")
            try:
                x = float(x)
                y = float(y)
                error = False
            except:
                error = True

    if operator == "+":
        print("The answer of", x, "plus", y, "is", x + y, ".")
    elif operator == "-":
        print("The answer of", x, "minus", y, "is", x - y, ".")
    elif operator == "*":
        print("The answer of", x, "times", y, "is", x * y, ".")
    elif operator == "/":
        print("The answer of", x, "divided by", y, "is", x / y, ".")
    else:
        print("Invalid operator. Please try again. \n")


def calculateAverage():
    '''prompt the user for the quantity of numbers to input, loop to calculate total and average, print the calculated average'''
    numQty = input("How many numbers would you like to enter?\n")

    #check to make sure a number was entered by converting it to an int data type.
    #if a number is not entered, a while loop will continue to prompt the user until a number is entered
    try:
        numQty = int(numQty)
    except:
        error = True
        while error:
            numQty = input("Invalid entry, please enter a number\n")
            try:
                numQty = int(numQty)
                error = False
            except:
                error = True

    totalsum = 0
    for iterVar in range(numQty):
        currentnumber = input("Enter a number:\n")

        #if input is invalid - we continue with another interation.  To ensure we are collected the correct number of variables
        #we reduce the iteration value
        try:
            currentnumber = float(currentnumber)
        except:
            error = True
            while error:
                currentnumber = input("Invalid entry, please enter a number\n")
                try:
                    currentnumber = float(currentnumber)
                    error = False
                except:
                    error = True

        totalsum = totalsum + float(currentnumber)

    print("Average = ", totalsum / numQty)

#welcome message
print("Welcome to the DSC 510 Calculator!")

#allow the user to run through the program until stop is typed.
operation = None
while operation != "stop":
    #prompt the user for the operation they want to perform
    operation = input("Enter a math operation to perform or 'stop' to quit: (+, - , * , / , avg)\n")

    #call performCalculation function for addition, subtraction or division
    #call calculateAverage function for average
    #if anything other than the preferred operators or 'stop' is entered, prompt the user again for a valid operation
    if operation in ("+", "-", "*", "/"):
        performCalculation(operation)
    elif operation == "avg":
        calculateAverage()
    elif operation != "stop":
        print("You have entered an incorrect value. Please try again")
        continue
