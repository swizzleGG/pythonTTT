import random

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]
currentPlayer = "X"
winner = None
gameRunning = True
inp = 0


#print the game board
def printBoard(board):
        print(board[0] + " " + board[1] + " " + board[2])
        print(board[3] + " " + board[4] + " " + board[5])
        print(board[6] + " " + board[7] + " " + board[8])

#take player input
def playerInput(board):
    inp = int(input("Please enter a number 1 to 9: "))
    if inp > 0 and inp < 10 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("That is not a valid option.")


#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checkTie(board):
    if "-" not in board:
        global gameRunning
        printBoard(board)
        print("GG! It's a tie.")
        gameRunning = False
        quit()
def checkWin(board):
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"GG! Player {currentPlayer} has won.")
        quit()

#switch player turns
def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer(board)


#game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer(board)
    computer(board)
    checkWin(board)
    checkTie(board)

