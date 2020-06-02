#This program will generate a random password based on how many number, lower/upper and specials they want in the password.

import random

#Specifics of password
print("Enter the following amounts for your random password. \n")
howManyNumbers = int(input("How many Numbers: "))
howManyLowerletters = int(input("How many lower case letters: "))
howManyUpperletters = int(input("How many upper case letters: "))
howManySpecial = int(input("How many Special Characters: "))
#print(howManyNumbers, howManyLowerletters, howManyUpperletters, howManySpecial)

#Declaring Vars for passwords
passwordNum = ('')
passwordLetter = ('')
passwordUpperLetter = ('')
fullScramPass = ''

#Number,Letter,Character lists
numbers = (0,1,2,3,4,5,6,7,8,9)
numOfNums = len(numbers) - 1

lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numOfLetter = len(lowerLetters) - 1

specialLetters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']
numOfSpecial = len(specialLetters) - 1
#print(numOfLetter, numOfSpecial)


#function to generate the numbers of the password
def numGen():
    global howManyNumbers, passwordNum
        #Running number loop until the user specific number = 1
    while howManyNumbers >= 1:
            #Setting teh random index to how many numbers are possible.
        index = random.randint(0,9)
        #print(numbers[index])
            #Adding the random number to the users number password variable.
        passwordNum += str(numbers[index])
            #subtracting 1 from the amount of numbers requested
        howManyNumbers -= 1


#function to generate the lower letters of the password
def getRandomChars(numOfLetters, charList, range):
    passwordLetter = ''
    #print("Number of letters wanted: " + str(numOfLetters))
        #Running number loop until the user specific number = 1
    while numOfLetters >= 1:
        #print("Number of letters WHILE: " + str(numOfLetters))
            #Setting the random index to how many chars are possible.
        index = random.randint(0, range)
        #print(charIndex[index])
            #Adding the random number to the users number password variable.
        passwordLetter += str(charList[index])
            #subtracting 1 from the amount of numbers requested
        numOfLetters -= 1
    return passwordLetter



numGen()
# Example hwo to call the function: VariableToHaveGenList = Fucntion"lowerLetterGet"(Arg1"HowManyOfThisTypeToGenerate", Arg2"ListOfChar", Arg3"HowManyCharForIndexOfWHileLoop")

doneLowerLetters = getRandomChars(howManyLowerletters, lowerLetters, numOfLetter)

#Converting the lower case
doneUpperLetters = getRandomChars(howManyUpperletters, lowerLetters, numOfLetter).upper()
doneSpecial = getRandomChars(howManySpecial,specialLetters, numOfSpecial)
#print(passwordNum, doneLowerLetters, doneUpperLetters, doneSpecial)

#Generating the scrambled full password
fullUnscramPass = passwordNum + doneLowerLetters + doneUpperLetters + doneSpecial


#print("UNSCRAM-Pass VAR: " + fullUnscramPass)


#range = len(fullUnscramPass)


while True:
        #Getting the lenght of UnScrambled Password
    range = len(fullUnscramPass)
    range -= 1
    #print("this IS the range var: " + str(range))
    if range < 0:
        #print("---------Range VAR IS: {}".format(range))
        break

        #Getting a random INT from 0 to the Range of UnScrambled Password.
    index2 = random.randint(0, range)
    #print(index2)
    #print("That is the INDEX2 Var")

    #print("This is the random index generated: {}").format(index2)

        #Adding The random CHAR from UnScram to FullScram password string.
    fullScramPass += fullUnscramPass[index2]
    #print("This is teh full pass being made : " + fullScramPass)

        #Removing that CHAR from the UnscamPassword string that way it doesnt get used again.
    fullUnscramPass = fullUnscramPass[:index2] + fullUnscramPass[index2 + 1:]
    #print("This is the unscam pass being made smaller: " + fullUnscramPass)

        #Minus 1 from the index.
    #index2 -= 1
        # Ending loop if index2 = 0


print("Random Password: " + fullScramPass)