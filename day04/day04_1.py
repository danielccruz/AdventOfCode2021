
from functools import reduce


boards = []
tmp_board = []


def get_board_score(board: list) -> int:
    total = 0
    #Update board with new drawn value
    for board_line in board:
        total += sum(filter(lambda x: x != -1, board_line))
    return total
                
                
def check_if_win(board: list, drawn_val: int) -> int:
    #Update board with new drawn value
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == drawn_val:
                board[i][j] = -1
    
    #Checks if row as a win
    for row in board:
        temp_row = row
        if len(list(filter(lambda x: x != -1, temp_row)))==0:
            return get_board_score(board)
    
    #Checks if column as a win
    for i in range(0,len(board[0])):
        if board[0][i] == -1:
            for j in range(1, len(board)):
                if board[j][i] == -1:
                    if j == len(board) -1:
                        return get_board_score(board)
                    continue
                else:
                    break
    return 0
                
with open('AdventOfCode2021/day04/day04.input', 'r+') as f:
    drawn_numbers = list(map(int,f.readline().strip().split(',')))
    f.readline()
    for line in f.readlines():
        if line == '\n':
            boards.append(tmp_board)
            tmp_board = []
        else:
            tmp_board.append(list(map(int, filter(lambda x: x != '', line.strip().split(' ')))))
    boards.append(tmp_board)
    
    for drawn in drawn_numbers:
        for board in boards:
            score = check_if_win(board, drawn)
            if score != 0:
                print('Last drawn number: ', drawn)
                print('Winner board: ', board)
                print('Found a board with a win. Score is:', score,'*',drawn,'=',score*drawn)
                exit()
        
        
        
        
