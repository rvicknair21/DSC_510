#File: Assignment_10_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: May 19, 2019
#Course: DSC 510
#Usage: Use an API to randomly feed the user Chuck Norris Jokes


def get_jokes(jokeURL):
    '''This function requests a joke from the Chuck Norris random joke generator and displays it to the user'''
    response = requests.request("GET", jokeURL)     #get a random joke from the API

    #embed the parsing statements in a try/except block in case there was an error when connecting to the web service
    try:
        json_data = json.loads(response.text)       #read the response text into a json string
        print("\n", json_data['value'], "\n")       #display the joke to the user
    except:             #if the response from the server was not successful, notify the user and exit the program.
        print("An error has been encountered while retrieving your joke.\n")
        exit()


import requests
import json

print("Hi! Welcome to the Chuck Norris random joke generator.\n")

tellajoke = True        #initialize loop control variable
url = "https://api.chucknorris.io/jokes/random"     #URL for random joke generator

while tellajoke:
    #ask if the user wants to hear a joke
    user_input = input("Would you like to hear a Chuck Norris joke?\n")

    #validate the user input, y, n, yes or no are accepted.  their response is converted to all lowercase before validating
    if user_input.lower() == "y" or user_input.lower() == "yes":
        get_jokes(url)      #calls the function to request a joke and display it
    elif user_input.lower() == "n" or user_input.lower() == "no":
        tellajoke = False
        print("\nThanks for playing!  Have a nice day :)")
    else:
        print("You have entered an incorrect response.  Only Yes and No accepted. Please try again.")
