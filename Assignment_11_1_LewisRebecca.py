#File: Assignment_11_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: May 26, 2019
#Course: DSC 510
#Usage: Build a cash register to allow a user to add items and calculate a total using a class

#Class to handle cash register functions
class CashRegister():

    #constructor
    def __init__(self):
        self.itemCount = 0
        self.cartTotal = 0

    #add an item to the cart
    def addItem(self, price):
        self.itemCount = self.itemCount + 1
        self.cartTotal = self.cartTotal + price

    #empty the cart
    def emptyCart(self):
        self.itemCount = 0
        self.cartTotal = 0

    #get the count of items
    def getCount(self):
        return self.itemCount

    #get the total amount of the cart
    def getTotal(self):
        return self.cartTotal

#function to print the current status of the cart since I'm printing these lines in multiple cases
def printCartUpdate(cart):
    print("\nYou have {} items in your cart.".format(cart.getCount()))
    print("The total of your cart is {}".format(locale.currency(cart.getTotal(), grouping=True)))

#main
import locale

locale.setlocale( locale.LC_ALL, 'English_United States.1252' )

#welcome message
print("Welcome to the Lewis General Store!\n")
myCart = CashRegister()     #create an instance of the cash register

userResponse = ''

#main control loop - runs until the user enters exit
while userResponse.lower() != 'exit':
    userResponse = input("\nEnter the price of the item you would like to add to your cart \n(Type exit to quit the program; Type empty to clear your cart):\n")

    if userResponse.lower() == 'exit':
        printCartUpdate(myCart)
        print("\nThank you for visiting the Lewis General Store!  Hope to see you again soon :)")
    elif userResponse.lower() == 'empty':
        myCart.emptyCart()
        print("\nYour cart has been emptied.")
    else:
        try:
            price = float(userResponse)
            myCart.addItem(price)
            printCartUpdate(myCart)
        except:
            print("\nYou have entered an invalid response.  Please try again.\n")
            continue




