"""
Simulate a battleship game.
Author: Johan Nino Espino
Creation Date: 01/09/2023
"""

#Import Section
import random

"""
Checks if a hit is made.

Parameter:
    row (int): an integer that represents the row the user selected between 0 and 7
    column (int): an integer that represents the column the user selected between 0 and 7
    board (2-D list): a two-dimensional list that represents the current board game of Battleships 

Returns:
    shipHit (bool): a boolean that return true if the value of board[row][column] is 1 or return false otherwise
"""

def check_hit(row, column, board):
    shipHit = False
    if board[row][column] == 1:
        print("The ship was hit!")
        shipHit = True
        board[row][column] = 2
    else:
        print("You miss the ship!")
        board[row][column] = 2
    return shipHit

"""
Counts the number of ships within one space of the miss.

Parameter:
    row (int): an integer that represents the row the user selected between 0 and 7
    column (int): an integer that represents the column the user selected between 0 and 7
    board (2-D list): a two-dimensional list that represents the current board game of Battleships 

Returns:
    -
"""
def close(row, column, board):
    shipsClose = 0
    spacesNearby = []
    if row == 0 and column == 0:
        spacesNearby.append(board[row][column + 1])
        spacesNearby.append(board[row + 1][column])
    elif row == 0 and column == 7:
        spacesNearby.append(board[row][column - 1])
        spacesNearby.append(board[row + 1][column])
    elif row == 7 and column == 0:
        spacesNearby.append(board[row][column + 1])
        spacesNearby.append(board[row - 1][column])
    elif row == 7 and column == 7:
        spacesNearby.append(board[row][column - 1])
        spacesNearby.append(board[row - 1][column])
    elif row == 0:
        spacesNearby.append(board[row][column - 1])
        spacesNearby.append(board[row][column + 1])
        spacesNearby.append(board[row + 1][column])
    elif row == 7:
        spacesNearby.append(board[row][column - 1])
        spacesNearby.append(board[row][column + 1])
        spacesNearby.append(board[row - 1][column])
    elif column == 0:
        spacesNearby.append(board[row - 1][column])
        spacesNearby.append(board[row + 1][column])
        spacesNearby.append(board[row][column + 1])
    elif column == 7:
        spacesNearby.append(board[row - 1][column])
        spacesNearby.append(board[row + 1][column])
        spacesNearby.append(board[row][column - 1])
    else:
        spacesNearby.append(board[row - 1][column])
        spacesNearby.append(board[row + 1][column])
        spacesNearby.append(board[row][column - 1])
        spacesNearby.append(board[row][column + 1])
    for spaces in spacesNearby:
        if spaces == 1:
            shipsClose += 1
    print("Miss at row " + str(row) + " and column " + str(column) + " , there are " + str(shipsClose) + " ships nearby.")

"""
Creates a list of ships left un-hit at the end of the game.

Parameter:
    board (2-D list): a two-dimensional list that represents the current board game of Battleships 

Returns:
    unHitShips (list): a list of coordinates that represents the ships that are still standing
"""
def unhit_ships(board):
    unHitShips = []
    row = 0
    while row < 8:
        column = 0
        while column < 8:
            if board[row][column] == 1:
                coordinates = "(" + str(row) + " , " + str(column) + ")"
                unHitShips.append(coordinates)
            column += 1
        row += 1
    return unHitShips

#Main Program

#Create a new board
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

#Initalize the variable and list
ships = 0
shipsCodeCoordinates = []

while ships < 8: #Loops until eight ships are created
    row = random.randint(0, 7) #Randomize the row that the ship would be located
    column = random.randint(0, 7) #Randomize the column that the ship would be located
    #This variable combines the row and column number to form a unique code to ensure no repeated coordinates
    codeCoordinates = str(row) + str(column)
    while codeCoordinates in shipsCodeCoordinates: #Loops when there is a repeated coordinates
        row = random.randint(0, 7) #Randomize the row that the ship would be located
        column = random.randint(0, 7) #Randomize the column that the ship would be located
        #This variable combines the row and column number to form a unique code
        codeCoordinates = str(row) + str(column)
    shipsCodeCoordinates.append(codeCoordinates) #Add the ship coordinate in a list
    board[row][column] = 1 #Change the value to one which represents where the ships are located in the board
    ships += 1 #Increment the ship value by one

#Initalize the variables and list
turns = 1
userGuessCoordinates = []
hit = 0

while turns <= 20 and hit < 8: #Loops until the user reach over ten turns or when the user hit all eight ships
    print("You on turn " + str(turns)) #Notify the user of the turn they are on
    print("Used coordinates: " + str(userGuessCoordinates)) #Print the list of used coordinates
    guessRow = int(input("Please choose a row between 0 and 7: ")) #The user enters a row they want to guess
    #The user enters a column they want to guess
    guessColumn = int(input("Please choose a column between 0 and 7: "))
    #Create a string that represents the coordinates that the user entered
    guessCoordinates = "(" + str(guessRow) + " , " + str(guessColumn) + ")"
    #Loops when the coordinates had already been used or when the row and column the user enter is not in 0 - 7
    while guessCoordinates in userGuessCoordinates or (guessRow < 0 or guessRow > 7) or (guessColumn < 0 or guessColumn > 7):
        #The user enters a row they want to guess
        guessRow = int(input("Remember to enter a row between 0 and 7: "))
        #The user enters a column they want to guess
        guessColumn = int(input("Remember to enter a column between 0 and 7: "))
        #Create a string that represents the coordinates that the user entered
        guessCoordinates = "(" + str(guessRow) + " , " + str(guessColumn) + ")"
    userGuessCoordinates.append(guessCoordinates) #Add the coordinate in the list
    #Check if the user made a hit or not and print out a statement
    hitOrMiss = check_hit(guessRow, guessColumn, board)
    if hitOrMiss == True: #The user made a hit
        hit += 1 #Increment the hit variable by one
    else: #The user miss the ship
        close(guessRow, guessColumn, board) #Prints out the number of ships that are nearby the miss
    turns += 1 #Increment the turns variable by one

unHitShipsCoordinates = unhit_ships(board) #Store a list of coordinates that the remaining ships are located
#Print out the list of coordinates that the remaining ships are located
print("Ships that are still standing are in coordinates: " + str(unHitShipsCoordinates))

standing = 8 - int(hit) #Calculate the number of ships that are still standing
#Print out the number of ships that are hit and the number of ships that are still standing
print("You hit a total of " + str(hit) + " ships. There are " + str(standing) + " ships still standing.")
