###################################
#File name: Text_Analyzer.py
#Created by: Ard Aunario
#Date created: 9/2/19
#Description: This program analyzes the texts
# of a file. It has the option to show the
# contents of the file, number of character,
# total words, or show percentage of each letters. 
###################################
###################################

fileName = input("Enter file name: ")

keepGoing = True

try:
    file = open(fileName, "r")
    fileCont = file.read()    #Contains the contents in the file
except FileNotFoundError:
    print("The file " + fileName + " was not found.")
finally:
    try:
        file.close()
    except NameError:     #If file doesn't exist, don't run program
        keepGoing = False

while(keepGoing):
    try:
        # Menu #
        print("\nMenu: ")
        print("1: Show contents of the file.")
        print("2: Count number of times a character appears.")
        print("3: Count total words in the file.")
        print("4: Show percentage each letter appeared on file.")
        print("5: Exit")
        userChoice = int(input("Enter choice: "))

        # Option 1 : Show contents #
        def displayFile():
            print(fileCont)

        # Option 2 : Count number of characters #
        def countChar(char):
            count = 0
            for c in fileCont:
                if c.lower() == char.lower():
                    count += 1
            return count
            
        # Option 3 : Number of words #
        def countWords():
            import re
            wordTotal = len(re.findall(r'\w+', fileCont))
            return wordTotal
            
        # Option 4 : Percentage of each letter used #
        def charPercent():
            for l in "abcdefghijklmnopqrstuvwxyz":
                perc = (countChar(l)/(len(fileCont) - countChar(" "))) * 100
                print("{0} - {1}%".format(l, round(perc, 2)))

        # Performing user request #
        if userChoice == 1:
            displayFile()
        elif userChoice == 2:
            try:
                userChar = str(input("Enter the character: "))
                print(str(countChar(userChar)) + " times the character appeared.")
            except TypeError:
                print("Invalid Input: Not a valid character.")
        elif userChoice == 3:
            print(str(countWords()) + " total words.")
        elif userChoice == 4:
            charPercent()
        elif userChoice == 5:
            print("Goodbye!")
            keepGoing = False       
    except ValueError:
        print("Input Error: Not one of the choices")
        
        
