#File: Assignment_7_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: May 4, 2019
#Course: DSC 510
#Usage: Open a file, create a dictionary of words, count the occurrence of the words and print

#add a word
def add_word(addword, addDict):
    '''This function determines whether the word is in the dictionary passed as parameters.  Different actions are taken depending
on if the word is in the dictionary already'''

    if addword not in addDict:        #if the word is not in the dictionary, add the word and start the count
        addDict[addword] = 1
    else:                           #if it is in the dictionary, increase the count
        addDict[addword] += 1

#process line
def process_line(procline, procdict):
    '''This function cleans up the line passed as a parameter by removing punctuation, spaces and blank lines and converts
all letters to lowercase.  It splits the line into words and calls the addword function for each one'''
    procline = procline.rstrip()
    procline = procline.lower()     #convert all letters to lowercaae since upper and lower are considered different values
    procline = procline.translate(procline.maketrans('', '', string.punctuation))     #remove punctuation

    #split the line into words
    words = procline.split()

    #for each word, call the add word function to determine whether to increment or add the word
    for word in words:
        add_word(word, procdict)


#pretty print
def pretty_print(printDict):
    '''This functions formats the completed dictionary into a printable format.  The dictionary is sorted in descending order
by word count and displayed with a header.  The total word count and dictionary count are also calculated for printing'''

    #initialize variables for counting words to print
    totalwordcount = 0
    dictionarylength = 0
    sortedWords = list()        #the dictionary will be converted to a list of tuples for sorting.  List is initialized here

    #switch the key and value to sort by count of words
    for key, val in list(printDict.items()):
        totalwordcount += val           #increment the total word count by adding each value
        dictionarylength += 1           #increment the dictionary count by adding 1
        sortedWords.append((val,key))   #switch the key and value

    sortedWords.sort(reverse = True)    #sort the list by the new key

    #print the headers
    print('''Length of Dictionary:\t{0} 
Total Word Count:\t\t{2}

{3: <17}\tCount
{1:_^25}'''.format(dictionarylength, '', totalwordcount, "Word"))

    #print the contents of the dictionary
    for key, value in sortedWords:
         print('{0: <17}\t{1}'.format(value,key))


#main function
import os
import string

#Open the File; if it can't be found, notify the user and exit the program
try:
    sourcefile = open('gettysburg.txt', 'r')
except:
    print('File cannot be found. Please place gettysburg.txt in the current directory', os.getcwd())
    exit()

filedict = dict()
for line in sourcefile:
    #for each line in the file
    process_line(line, filedict)

#call the function to print the dictionary
pretty_print(filedict)
