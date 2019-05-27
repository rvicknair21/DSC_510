#File: LewisRebecca_Assignment_4_1.py
#Name: Rebecca Lewis
#Date: April 7, 2019
#Course: DSC 510
#Usage: Retrieve information from the user to calculate installation cost for fiberoptic cable and print a receipt; use
#conditional statements to check for errors and calculate sliding scale pricing in a function

#function to calculate cost
def calc_cost(feet, unitprice):
    return feet * unitprice   #calculate return total cost calculation

#Welcome Message
print("Hi There! Today I'm going to help you calculate the cost of installing fiber optic cable for your company.")

#Retrieve the name of the company
company_name = input("What is the name of your company?\n")

#retrieve the number of feet of cable will be installed
user_input = input("\nWhat length of cable needs to be installed in feet?\n")

#calculate total cost
#use try and except to check for a valid entry from the user
try:            #try converting to a float
    number_feet = float(user_input)
except:         #print message to user and exit execution
    print("Input is invalid. Please run again and enter a number.")
    exit()

#calculate the cost using sliding scale
#if the customer purchase more than 100 feet of cable, cost is .80
if number_feet > 100:
    cost = .80
    if number_feet > 250:   #if they purchase more than 250, the cost is .70
        cost = .70
        if number_feet > 500:   #if they purchase more than 500, the cost is .50
            cost = .50
else:                           #if they purchase less than or equal to 100, the cost is .87
    cost = .87


final_cost = calc_cost(number_feet, cost)

#print receipt
print("\nInstallation Receipt for ", company_name)
print("________________________________________\n")
print('{:0.2f}'.format(number_feet), "ft of cable at",'${:,.2f}'.format(cost), "per foot")
print("Total = ", '${:,.2f}'.format(final_cost))
print("________________________________________\n")
print("Thank you for your business!")
