import random

#SHOW TIC TAC TOE LAYOUT
def instructions():
    print("===WELCOME TO THE TIC-TAC-TOE CHAMPIONSHIPS===")
    print("BOARD ORIENTATION")
    print('---------------')
    print('| ' + str(7) + ' || ' + str(8) + ' || ' + str(9) + ' |')
    print('---------------')
    print('| ' + str(4) + ' || ' + str(5) + ' || ' + str(6) + ' |')
    print('---------------')
    print('| ' + str(1) + ' || ' + str(2) + ' || ' + str(3) + ' |')
    print('---------------')

    print("\nCHOOSING WHO GOES FIRST")
    print("1 - COMPUTER (HOST)")
    print("2 - PLAYER / COMPUTER")

#PRINTS OUT THE BOARD
def display_board(board):
    print('---------------')
    print('| ' + board[7] + ' || ' + board[8] + ' || ' + board[9] + ' |')
    print('---------------')
    print('| ' + board[4] + ' || ' + board[5] + ' || ' + board[6] + ' |')
    print('---------------')
    print('| ' + board[1] + ' || ' + board[2] + ' || ' + board[3] + ' |')
    print('---------------')

#CHOOSE WHICH CHARACTER
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        #print("Choose either X or O: ")
        letter = input("Choose either X or O: ").upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

#WHO GOES FIRST
def FirstMove(turn):
    if turn == 1:
        return 'COMPUTER (HOST)'
    elif turn == 2:
        return 'PLAYER / COMPUTER'

#RESTART GAME
def PlayAgain():
    print("DO YOU WANT TO PLAY AGAIN? (YES OR NO) ")
    return input().lower().startswith('y')

#RECORD MOVE
def RecordMove(board, letter, move):
    board[move] = letter

#DETERMINE WINNER
def Winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or #TOP
            (board[4] == letter and board[5] == letter and board[6] == letter) or #MID
            (board[1] == letter and board[2] == letter and board[3] == letter) or #BOT
            (board[7] == letter and board[4] == letter and board[1] == letter) or #LEFT
            (board[8] == letter and board[5] == letter and board[2] == letter) or #MIDDLE
            (board[9] == letter and board[6] == letter and board[3] == letter) or #RIGHT
            (board[7] == letter and board[5] == letter and board[3] == letter) or #DIAGONAL LEFT
            (board[9] == letter and board[5] == letter and board[1] == letter)) #DIAGONAL RIGHT

#MAKE A COPY OF THE BOARD TO USE
def CopyBoard(board):
    duplicate = []

    for i in board:
        duplicate.append(i)

    return duplicate

#CHECK IF SPACE IS FREE
def FreeSpace(board, move):
    return board[move] == ' '

#GET OPPONENT MOVE
def OppoMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FreeSpace(board, int(move)):
        #print("Enter next move (1-9): ")
        move = input("Enter next move (1-9): ")
    return int(move)

#=================Level 2====================#
#RANDOM MOVE
def RandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if FreeSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#GET HOST MOVE
def CompMove(board, comp_letter):
    if comp_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    #CHECK BOARD IF HOST CAN WIN
    for i in range(1, 10):
        copy = CopyBoard(board)
        if FreeSpace(copy, i):
            RecordMove(copy, comp_letter, i)
            if Winner(copy, comp_letter):
                return i

    #BLOCK OPPONENT MOVE IF WINNING
    for i in range(1, 10):
        copy = CopyBoard(board)
        if FreeSpace(copy, i):
            RecordMove(copy, player_letter, i)
            if Winner(copy, player_letter):
                return i

    #STRATEGY 1: SECURE MIDDLE (4 POSSIBLE WINNING MOVES)
    if FreeSpace(board, 5):
        return 5

    #STRATEGY 2: SECURE CORNERS (3 POSSIBLE WINNING MOVES PER CORNER)
    move = RandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    #STRATEGY 3: FILL IN BLANK SPACES
    return RandomMove(board, [2, 4, 6, 8])
#=================Level 2====================#

def isBoardFull(board):
    for i in range(1, 10):
        if FreeSpace(board, i):
            return False
    return True

def main():
    instructions()

    while (True):
        #RESET BOARD
        board = [' '] * 10
        player_letter, comp_letter = inputPlayerLetter()
        going_first = int(input("WHO GOES FIRST? "))
        turn = FirstMove(going_first)
        print("THE " + turn + " WILL GO FIRST")
        ongoingGame = True

        while (ongoingGame):
            if turn == 'PLAYER / COMPUTER':
                display_board(board)
                move = OppoMove(board)
                RecordMove(board, player_letter, move)

                if Winner(board, player_letter):
                    display_board(board)
                    print("COMPUTER (HOST) ACCEPTS DEFEAT")
                    print("YOU WON THE GAME")
                    ongoingGame = False
                else:
                    if isBoardFull(board):
                        display_board(board)
                        print("IT'S A TIE")
                        print("YOU ARE A WORTHY OPPONENT")
                        break
                    else:
                        turn = 'COMPUTER (HOST)'
            else:
                move = CompMove(board, comp_letter)
                RecordMove(board, comp_letter, move)

                if Winner(board, comp_letter):
                    display_board(board)
                    print("THE COMPUTER (HOST) WINS")
                    print("YOU LOSE")
                    ongoingGame = False
                else:
                    if isBoardFull(board):
                        display_board(board)
                        print("IT'S A TIE")
                        print("YOU ARE A WORTHY OPPONENT")
                        break
                    else:
                        turn = 'PLAYER / COMPUTER'

        if not PlayAgain():
            break

if __name__ == '__main__':
    main()