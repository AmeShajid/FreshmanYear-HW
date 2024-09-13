#Ame Shajid
#Feb 27 2024
'''
First, ask the player for the size of the board. This number must be between 3 and 7 (inclusive). If the player gives a number outside that range, or a non-numeric value ask again.
Print out the rules and show the board with each space labeled.
Ask the player to enter the correct number of spaces. If the answer is outside the range or non-numeric ask again.
Print the board with the positions the player selected displayed. Print the distances measurements.
Print out if the player won or lost.
If the player does not pick unique spaces, they lose automatically.
'''

def getInteger(question, a, b):
    # This function gives the user with a question and then it check that the input is an integer within the range.
    while True:
        value = input(question)
        if value.isdigit():
            value = int(value)
            if a <= value <= b:
                return value
            else:
                print("Number outside of range")
        else:
            print("You did not enter a number")

def printOptions(n):
    # This function prints the possible spaces on the board based on the size
    for i in range(n*n):
        print(i, end=" ")
        if (i+1) % n == 0:
            print()

def distance(i, j, n):
    # This function calculates the distance between the two spaces on the board
    x1, y1 = i % n, i // n
    x2, y2 = j % n, j // n
    #right here is the square root part I coudlve import math but multiplying works
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def checkBoard(board, n):
    # It checks whether the number of selected positions is equal to n
    # It then calculates the distances between all pairs of selected positions and ensures that they are all unique. towards the end has win/lose
    # this part got super tricky for me im not gonna lie
    positions = [i for i in range(n) if board[i] == 1]
    if len(positions) != n:
        return False
    distances = [distance(positions[i], positions[j], n) for i in range(n) for j in range(i+1, n)]
    if len(distances) == len(set(distances)):
        return True
    else:
        return False
# there was some parts It got difficult for me
if __name__ == "__main__":
    # Main part of the game. this is the questions and rules
    print("Welcome to Placement Game")
    size = getInteger("Enter Size of Board (between 3 and 7): ", 3, 7)
    print("Rules:")
    print("You must pick 3 spaces on the board to place ones.")
    print("The distances between all the ones you placed must be different.")
    print("The possible spaces are shown below.")
    printOptions(size)

    positions = []
    print("Pick 3 spaces")
    # User selects 3 spaces on the board, and the selections are checked.
    for _ in range(size):
        valid_input = False
        while not valid_input:
            pick = input("Pick Space (0-" + str(size*size-1) + "): ")
            if pick.isdigit():
                pick = int(pick)
                if 0 <= pick < size*size:
                    if pick not in positions:
                        positions.append(pick)
                        valid_input = True
                else:
                    print("Number outside of range.")
            else:
                print("You did not enter a number.")

    # Creates a board based on user inputs.
    board = [1 if i in positions else 0 for i in range(size*size)]
    print("Your board is shown below")
    for i in range(size*size):
        print(board[i], end=" ")
        if (i+1) % size == 0:
            print()

    # Check and print the distances between selected positions.
    print("We will check the distance between all selections")
    for i in range(size):
        for j in range(i+1, size):
            dist = distance(positions[i], positions[j], size)
            print(f"The distance from {positions[i]} to {positions[j]} is {dist:.3f}")
    # Check if the board configuration passes the game rules.
    if checkBoard(board, size):
        print("You Win: Your Board Passes the Test")
    else:
        print("You Lose: Your board contained multiple placements with the same distance")
