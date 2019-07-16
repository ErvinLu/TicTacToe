from math import inf as infinity
from random import choice

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

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

#RESTART GAME
def PlayAgain():
    print("DO YOU WANT TO PLAY AGAIN? (YES OR NO) ")
    return input().lower().startswith('y')

def evaluate(board):
    """
    Function to heuristic evaluation of board.
    :param board: the board of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(board, COMP):
        score = +1
    elif wins(board, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(board, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param board: the board of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_board = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in win_board:
        return True
    else:
        return False


def game_over(board):
    """
    This function test if the human or computer wins
    :param board: the board of the current board
    :return: True if the human or computer wins
    """
    return wins(board, HUMAN) or wins(board, COMP)


def empty_cells(board):
    """
    Each empty cell will be added into cells' list
    :param board: the board of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(board, depth, player):
    """
    AI function that choice the best move
    :param board: current board of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see aiturn() function)
    :param player: a human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, -1, score]

    for cell in empty_cells(board):
        x, y = cell[0], cell[1]
        board[x][y] = player
        score = minimax(board, depth - 1, -player)
        board[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    print("MINIMAX BEST SCORE: " + str(best))
    return best

def render(board, c_choice, h_choice):
    """
    Print the board on console
    :param board: current board of the board
    """
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in board:
        for cell in row:
            symbol = chars[cell]
            #print('| {symbol} |', end='')
            print("| " + symbol + " |", end = '')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it chooses a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [2, 0], 2: [2, 1], 3: [2, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [0, 0], 8: [0, 1], 9: [0, 2],
    }

    while move < 1 or move > 9:
        move = int(input("Enter next move (1-9): "))
        coord = moves[move]
        can_move = set_move(coord[0], coord[1], HUMAN)

        if not can_move:
            print('Bad move')
            move = -1


def main():
    """
    Main function that calls all functions
    """
    instructions()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        h_choice = input("Choose either X or O: ").upper()

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    while first != 1 and first != 2:
        first = int(input("WHO GOES FIRST: "))

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 1:
            ai_turn(c_choice, h_choice)
            first = ''

        render(board, c_choice, h_choice)

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        render(board, c_choice, h_choice)
        print("COMPUTER (HOST) ACCEPTS DEFEAT")
        print("YOU WON THE GAME")
    elif wins(board, COMP):
        render(board, c_choice, h_choice)
        print("THE COMPUTER (HOST) WINS")
        print("YOU LOSE")
    else:
        render(board, c_choice, h_choice)
        print("IT'S A TIE")
        print("YOU ARE A WORTHY OPPONENT")
    exit()


if __name__ == '__main__':
    main()