#File: LewisRebecca_Assignment_2_1.py
#Name: Rebecca Lewis
#Date: March 23, 2019
#Course: DSC 510
#Usage: Retrieve information from the user to calculate installation cost for fiberoptic cable and print a receipt

#Welcome Message
print("Hi There! Today I'm going to help you calculate the cost of installing fiber optic cable for your company.")

#Retrieve the name of the company
company_name = input("What is the name of your company?\n")

#retrieve the number of feet of cable will be installed
number_feet = input("\nWhat length of cable needs to be installed in feet?\n")

#calculate total cost
total_cost = float(number_feet) * .87

#print receipt
print("\nInstallation Receipt for ", company_name)
print("________________________________________\n")
print(number_feet, "ft of cable at $0.87 per foot")
print("Total = $", str(total_cost))
print("________________________________________\n")
print("Thank you for your business!")
