#Ame Shajid
#Feburary 6 2024

#import math module
import math
# first function for validating the question
def getInteger(question):
    validData = False
    while not validData:
        number = input(question)
        if number.isdigit():
            number = int(number)
            if number > 0:
                validData = True
            else:
                print("Invalid Input\nInput must be a positive non-zero integer")
        else:
            print("Invalid Input\nInput must be a positive non-zero integer")
    return number
# next function for rabbits where we put in the foxes and rabbits values and do the equation
def nextRabbits(f, r):
    r = r + math.floor(r * (.04 - .0005 * f))
    return r
# next function for foxes where we put in the foxes and rabbits values and do the equation

def nextFoxes(f, r):
    f = f - math.floor(f * (0.2 - 0.00005 * r))
    return f
#right here is the main function
if __name__ == "__main__":
    rabbits = getInteger("Enter Number of Rabbits: ")
    foxes = getInteger("Enter Number of Foxes: ")
    question = getInteger("Enter Years to Simulate: ")

    print("| Years   | Foxes   | Rabbits |")
    print("| ------- | ------- | ------- |")
#right here is where we are putting it inside the grid thing. 
    for i in range(question + 1):
        rabbits1 = nextRabbits(foxes, rabbits)
        foxes1 = nextFoxes(foxes, rabbits)

        print(f'|   {i: >5} |  {foxes1: >6} | {rabbits1: >7} |')

        rabbits = rabbits1
        foxes = foxes1

#this spacing had me so messed up it actually took me so long to figure out how to get the spacing right i dont know why. 







