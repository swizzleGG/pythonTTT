# tic tac toe
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
board[0][0] = "x"
def print_board(board):
    for row in board:
        for slot in row:
            print(slot, end=" ")
        print()

def quit(user_input):
    if user_input.lower() == "q":
        return True
        print("Thanks for playing.")
    else: return False

def check_input(user_input):
    #check if number
    if not isnum(user_input): return True
    #check if 1 - 9
    if not iscorrectnum(user_input): return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("That is not a valid number.")
        return False
    else: return True

def iscorrectnum(user_input):
    if int(user_input) > 9:
        print("This number is out of bounds.")
        return False
    if int(user_input) < 0:
        print("This number is out of bounds.")
        return False
    else: return True

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col / 3)
    return(row,col)

def istaken(coords, board):
    row = coords[0]
    col = coords[0]
    if board[row][col] != "x":
        print("This position is already taken.")
        return True
    else: return False

while True:
    print_board(board)
    user_input = input("Please type a number 1 - 9 or 'q' to quit: ")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again. ")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue