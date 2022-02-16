import random

def main():
    n_games = 10000
    nx = 0
    no = 0
    nt = 0
    for i in range(n_games):
        winner = play_game()
        if winner == 'x':
            nx += 1
        elif winner == 'o':
            no += 1
        else:
            nt+= 1
    print(nx, no, nt)
    pts_x = nx +0.5*nt
    pts_o = no + 0.5*nt
    percent_x = 100.0 * pts_x / n_games
    percent_o = 100.0 * pts_o / n_games
    print('pts_x:', pts_x, 'pts_o:', pts_o)
    print('percent_x:', percent_x, 'percent_o:', percent_o)

def play_game():
    board = new_board()
    print_board(board)
    while True:
        play_computer_defensive(board, 'x')
        print_board(board)
        winner = find_winner(board)
        if winner != ' ' or board_is_full(board):
            break
        play_computer_opportunistic(board, 'o')
        print_board(board)
        winner = find_winner(board)
        if winner!= ' ' or board_is_full(board):
            break
    if winner == ' ':
        print('tie, nt, play again')
    else:
        print('the magnificent winner is', winner)
    return winner



        
def new_board():
    row0 = [' ', ' ', ' ']
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    board = [row0, row1, row2]
    return board

def print_board(board):
    print('-------')
    for row in board:
        for cell in row:
            print('|', end= "")
            print(cell, end="")
        print('|')
        print('-------')

def set_cell(board, row, col, marker):
    board[row][col] = marker

def get_move(board, marker):
    """asks the player for a move and sets the appropriate cell"""
    valid = False
    while not valid:
        row, col = -1, -1
        while not row in [0, 1, 2]:
            row = int(input('row? '))
            while not col in [0, 1, 2]:
                col = int(input('col? '))
        if board[row][col] == ' ':
            valid = True
    set_cell(board, row, col, marker)

def play_computer_first_found(board, marker):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                #if it's blank, put my marker
                set_cell(board, row, col, marker)
                return

def play_computer_random(board, marker):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            set_cell(board, row, col, marker)
            return

def find3(row):
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    else:
        return ' '
def find_winner(board):
    for row in board:
        winner = find3(row)
        if winner != ' ':      #yay!
            return winner
    for col_no in range(3):
        col = extract_col(board, col_no)
        winner = find3(col)
        if winner != ' ':
            return winner
    slash = extract_slash(board)
    winner = find3(slash)
    if winner != ' ':
        return winner
    bslash = extract_bslash(board)
    winner = find3(bslash)
    if winner != ' ':
        return winner

    #if there is no winner, return a ' '
    return ' '

def extract_col(board, col_no):
    col = [board[0][col_no],
           board[1][col_no],
           board[2][col_no]]
    return col

def extract_slash(board):
    slash = [board[2][0],
             board[1][1],
             board[0][2]]
    return slash

def extract_bslash(board):
    bslash = [board[0][0],
              board[1][1],
              board[2][2]]
    return bslash

def board_is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def find_win_candidate(board, marker):
    """Scan each cell to see if marker has a possible victory on that cell. Return the thr row and colunm of the victory cell, as well as the winner marker or ' ' if there is no possible victory"""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                is_win = check_if_winning_move(board, row, col, marker)
                if is_win == marker:
                    return [row, col, is_win]
    return [None, None, None]

def check_if_winning_move(board, row, col, marker):
    set_cell(board, row, col, marker)
    winner = find_winner(board)
    set_cell(board, row, col, ' ')
    if winner == marker:
        return winner
    else:
        return ' '

def play_computer_defensive(board, my_marker):
    opp_marker = 'x' if my_marker == 'o' else 'o'
    [row, col, win_candidate] = find_win_candidate(board, opp_marker)
    if win_candidate == opp_marker:
        set_cell(board, row, col, my_marker)
    else:
        play_computer_random(board, my_marker)

def play_computer_opportunistic(board, marker):
    [row, col, win_candidate] = find_win_candidate(board, marker)
    if win_candidate == marker:
        set_cell(board, row, col, marker)
    else:
        play_computer_defensive(board, marker)
        
        
main()

