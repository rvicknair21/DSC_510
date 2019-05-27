#File: Assignment_6_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: April 20, 2019
#Course: DSC 510
#Usage: Accept a list of temperatures from the user, determine the smallest and largest values entered

def findMax(templist):
    '''iterate through a list of temperatures to find the maximum value'''

    maxtemp = 0
    for indx, temp in enumerate(templist):      #use enumerate to get the current index number in the loop
        if indx == 0 or temp > maxtemp:         #if we are on the first item in the list or a greater temperature
            maxtemp = temp
        else:
            continue

    return maxtemp

def findMin(templist):
    '''iterate through a list of temperatures to find the minimum value'''

    mintemp = 0                           #since we already know t
    for indx, temp in enumerate(templist):      #use enumerate to get the current index number in the loop
        if indx == 0 or temp < mintemp:         #if we are on the first item in the list or a lesser temperature
            mintemp = temp
        else:
            continue

    return mintemp

#create an empty list for temperatures
temperatures = []

#ask the user to input temperatures until a sentinel value is entered
while True:
    newtemp = input("Please enter a temperature. Type 'stop' when you done.\n")

    if newtemp != 'stop':
        #if the value entered is not a number or stop, alert the user and continue with the loop
        try:
            newtemp = float(newtemp)
        except:
            print("Invalid Entry.\n")
            continue

        #if the value entered is a number, add it to the list
        temperatures.append(float(newtemp))
    else:
        break

#find the largest and smallest temps
MaxTemperature = findMax(temperatures)
MinTemperature = findMin(temperatures)

#create multi line string to display temperatures
outString = """\nYou have entered {} temperatures.  
The maximum temperature is {}.  
The minimum temperature is {}.
All temperatures entered:"""

#print string with temperatures inserted
print(outString.format(len(temperatures), MaxTemperature, MinTemperature), temperatures)






