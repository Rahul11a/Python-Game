# Setting up the board
def display_board(board):
    #board =['#','X','O','X','O','X','O','X','O','X']
    print("     |     |     ")
    print("  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  ")
    print("_____|_____|______")
    print("     |     |     ")
    print("  "+board[4]+"  |  "+board[5]+"  |   "+board[6]+" ")
    print("_____|_____|______")
    print("     |     |     ")
    print("  "+board[1]+"  |  "+board[2]+"  |   "+board[3]+" ")
    print("     |     |     ")

# Taking the input  from the player
def player_input():
    '''
    Here OUTPUt is (player1_marker, player2_marker)
    :return:
    '''
    marker = ""
    while not marker =='X' or marker == 'O':
        marker = input("Player 1: Choose 'X' or'O': ").upper()
        if marker == "X":
            return ('X','O')
        elif marker == "O":
            return ('O','X')

# Placing the marker
def place_marker(board, position, marker):
    '''
    This places the marker at the location
    :param board:
    :param marker:
    :param position:
    :return:
    '''
    board[position] = marker

# Checking at every turn if any player has won
def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark)\
            or (board[4] == board[5] == board[6] == mark)\
            or board[7] == board[8] == board[9] == mark\
            or board[7] == board[5] == board[3] == mark\
            or board[1] == board[5] == board[9] == mark\
            or board[1] == board[4] == board[7] == mark\
            or board[2] == board[5] == board[8] == mark\
            or board[3] == board[6] == board[9] == mark:
        return True
    else:
        return False

# Randon function to choose who plays first
import random
def choice_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Checking if space is available for the mark or not
def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

# Checking if the board is full or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
     # Board is full
    return True

# Taking the input from the player
def player_choice(board):
    display_board(board)
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose the position from the left slots: "))
    return position

# To check if player wants to replay
def replay():
    choice = input("Do you want to replay? YES or NO:").upper()
    if choice == 'YES':
        return True
    else:
        return False

##################################
#        Driver Function         #
##################################

ch =''
play_game = ''
while True:
    board = [" "] * 10
    display_board(board)
    P1_marker, P2_marker = player_input()
    turn = choice_first()
    print(turn + " will play first")
    #while play_game != 'Y' or play_game != 'N':
    play_game = input("Ready to play? Y/N:").upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            # Display the board
            display_board(board)
            # choose a position
            pos = player_choice(board)
            # Place the mark
            place_marker(board, pos, P1_marker)
            if win_check(board, P1_marker):
                display_board(board)
                print("Player 1 Won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME !")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Display the board
            display_board(board)
            # choose a position
            pos = player_choice(board)
            # Place the mark
            place_marker(board, pos, P2_marker)
            if win_check(board, P2_marker):
                display_board(board)
                print("Player 2 Won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME !")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break

