import sys
from configparser import *


config = ConfigParser()
config.read('mass')


#Gathers user input.
mode = input("Welcome to the chemistry conversion center. \n "
            "If you would like to convert from moles to grams please enter (1).\n "
            "If you would like to convert from grams to moles please enter (2).\n "
            "If you would like the calculate to GFM please enter (3). ")



#Gets rid of invalid input.
def invalid(type,min,max) :
    if type == '':
        sys.exit("You have entered no input.")
    type = int(type)
    if type > max or type < min:
        print("Your input is invalid. The invalid input: ", type)
        print("The next time you use the code please use a value between", min, "and", max)
        sys.exit("Restart to try again.")
    else:
        print("✓")

def newRound(originalNumber):
    decimal = 1
    for character in originalNumber:
        if character == ".":
            decimal = True
        else:
            break
    if decimal == True:
        numbersBeforeDecimal = originalNumber.find(".")
        #Add that number plus 3 (for decimals), slice that from number string.
        numbersBeforeDecimal = numbersBeforeDecimal + 3
        threeDecimal = originalNumber[0:numbersBeforeDecimal]
        lastNumber = threeDecimal[-1]
        lastNumber = int(lastNumber)
        roundedNumber = threeDecimal[0:-1]
        roundedNumber = float(roundedNumber)

    #Take last number (3rd decimal place) convert it to integer string. Evaluate if less or more than 5.
        if lastNumber > 4:
            roundedNumber = roundedNumber + 0.01
        return(roundedNumber)
invalid(mode,1,3)

#Gets formula for chemical equation in problem.

print("I will now ask various questions to gather information about the element or compound you are solving.")
numberOfElements = input("How many different elements are there?")
invalid(numberOfElements,1,100)
numberOfElements = int(numberOfElements)


#Creates dictionary to store information about the equation.
dicOfElements = {}

indexForElement = 0


#Ask for input to complete the dictionary. format {atomic # : amount of element}
while indexForElement < numberOfElements:
    atomicInput = input("What's the atomic number of the element? ")
    invalid(atomicInput,1,109)
    atomicInput = int(atomicInput)
    subscriptInput = input("How many atoms are there of this element? ")
    invalid(subscriptInput,1,100)
    subscriptInput = int(subscriptInput)
    dicOfElements.update({atomicInput:subscriptInput})
    indexForElement = indexForElement + 1

GFM = 0.00
#Gathers info and stores in into a dictionary.
for key,value in dicOfElements.items():
    invalid(key, 1, 109)
    key = str(key)
    elementMass = config.get('mass_list', key)
    elementMass = float(elementMass)
    totalElementMass = float(int(value)) * elementMass
    GFM = GFM + totalElementMass
    roundedGFM = newRound(str(GFM))
print("The GFM is: ", roundedGFM, "g/mol")

def convert(direction,total):
    direction = int(direction)
    if direction == 1:
        moles = input("What's your given amount of moles that you need to convert from? ")
        moles = float(moles)
        invalid(moles,1.0,100.0)
        molesToGrams = moles * total
        roundedGrams = newRound(str(molesToGrams))
        print("The amount of grams is: ", roundedGrams, "g")
        sys.exit("Program complete.")
    if direction == 2:
        givenGrams = input("What's your given amount of grams that you need to convert from? ")
        givenGrams = float(givenGrams)
        invalid(givenGrams,1.0,100.0)
        gramsToMoles = givenGrams / total
        roundedMoles = newRound(str(gramsToMoles))
        print("The amount of moles is: ", roundedMoles, "moles")
        sys.exit("Program complete.")

convert(mode,GFM)
