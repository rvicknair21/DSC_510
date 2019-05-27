#File: Assignment_8_1_LewisRebecca.py
#Name: Rebecca Lewis
#Date: May 12, 2019
#Course: DSC 510
#Usage: Open a file, create a dictionary of words, count the occurrence of the words and write to a file


def add_word(addword, addDict):
    '''This function determines whether the word is in the dictionary passed as parameters.  Different actions are taken depending
on if the word is in the dictionary already'''

    if addword not in addDict:        #if the word is not in the dictionary, add the word and start the count
        addDict[addword] = 1
    else:                           #if it is in the dictionary, increase the count
        addDict[addword] += 1


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


def pretty_print(printDict):
    '''This functions formats the header for the dictionary into a pretty format.  The dictionary is sorted in descending order
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
    strFile = 'Length of Dictionary:\t{0}\nTotal Word Count:\t\t{2}\n\n{3: <17}\tCount\n{1:_^25}\n'.format(dictionarylength, '', totalwordcount, "Word")

    #format the contents into a string
    for key, value in sortedWords:
         strFile= '{0}{1: <17}\t{2}\n'.format(strFile,value,key)

    #call the process file function to print to a file
    process_file(strFile)


def process_file(file_string):
    '''prints formatted string and results of dictionary count to a file'''

    # loop is used to ensure the file name is valid once all of the symbols are stripped.  the user will be reprompted if it is not valid
    filename = ''
    while filename == '':
        #prompt the user for the filename and strip any punctuation and spaces
        filename = input('Enter a name for the output file:\n')
        filename = filename.replace(' ', '')
        filename = filename.translate(filename.maketrans('', '', string.punctuation))

        # if the filename is valid, proceed with writing the file.  If not alert the user
        if filename != '':
            with open('{}.txt'.format(filename), "w") as outputfile:
                outputfile.write(file_string)
        else:
            print('Invalid File Name.  Please use alphanumeric characters.')


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

#call the function to format the dictionary
pretty_print(filedict)

sourcefile.close()
