board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " ", ]

game_still_going = True

def play_game():
    i = 0
    print("WELCOME to tic-tac-toe game"
          "each player will get a chance but if any"
          "player will give wrong input"
          "then turn will be given to opponent")
    while i<9:
        display_board()
        x = print("\t\t player 1 enter : ")
        player1()

        print("\t\t player 2 enter : ")
        y = player2()

    i = i+1

"......................functions............................."

def display_board():
    print(board[0] + " | ", board[1] + " | ", board[2] + " | ")
    print(board[3] + " | ", board[4] + " | ", board[5] + " | ")
    print(board[6] + " | ", board[7] + " | ", board[8] + " | ")

def player1():
    try:
        player1 = int(input("choose a position between 1 to 9 : ")) - 1
        if board[player1] == " ":
            board[player1] = "x"
            display_board()
            check()
        else:print("place is already filled")
    except Exception as e:
        print("invalid input so turn is given to y")


def player2():
        try:
            player2 = int(input("choose a position between 1 to 9 : ")) - 1
            if board[player2] == " ":
                board[player2] = "o"
                display_board()
                check()
            else:print("No space available")
        except Exception as e:
            print("invalid input so turn is given to x")

def check_board(board):
    pass


def check():
    # ............................ROWS.....................
    if (board[0] == board[1] == board[2] == "x"):
        print("winner is x ")
        exit()
    elif (board[0] == board[1] == board[2] == "o"):
        print("winner is o ")
        exit()
    elif (board[3] == board[4] == board[5] == "x"):
        print("winner is x ")
        exit()
    elif (board[3] == board[4] == board[5] == "o"):
        print("winner is o ")
        exit()
    elif (board[6] == board[7] == board[8] == "x"):
        print("winner is x ")
        exit()
    elif (board[6] == board[7] == board[8] == "o"):
        print("winner is o ")
        exit()
    # .................................COLUMNS...........................
    elif (board[0] == board[3] == board[6] == "x"):
        print("winner is x ")
        exit()
    elif (board[0] == board[3] == board[6] == "o"):
        print("winner is o ")
        exit()
    elif (board[1] == board[4] == board[7] == "x"):
        print("winner is x ")
        exit()
    elif (board[1] == board[4] == board[7] == "o"):
        print("winner is o ")
        exit()
    elif (board[2] == board[5] == board[8] == "x"):
        print("winner is x ")
        exit()
    elif (board[2] == board[5] == board[8] == "o"):
        print("winner is o ")
        exit()
    # ...............................DIAGONAL................................
    elif (board[0] == board[4] == board[8] == "x"):
        print("winner is x ")
        exit()
    elif (board[0] == board[4] == board[8] == "o"):
        print("winner is o ")
        exit()
    elif (board[2] == board[4] == board[6] == "x"):
        print("winner is x ")
        exit()
    elif (board[2] == board[4] == board[6] == "o"):
        print("winner is o ")
        exit()
play_game()
