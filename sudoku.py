# Simple Sudoku puzzle game using backtracking algorithm to solve.
import numpy as np

# Current sudoku board, 0's indicate a empty spot on the board.
board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 2, 0, 0, 5, 0, 7, 6, 0],
         [0, 6, 0, 0, 0, 0, 0, 0, 3],
         [5, 0, 0, 0, 0, 0, 2, 0, 7],
         [0, 3, 0, 0, 1, 0, 0, 0, 0],
         [2, 0, 0, 4, 0, 0, 0, 3, 0],
         [0, 0, 0, 6, 0, 0, 0, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 2, 7, 0, 0, 4, 0]]

# Given x for row and y for column, check if number in x,y is valid for location.
def validation(x, y, num):
    global board
    
    # Validate for row, column
    for i in range(9):
        if board[x][i] == num:
            return False
        
        elif board[i][y] == num:
            return False
        
    # Validate for 9x9 square.
    # Round down and multiply by 3 to get current 3x3 square for given location.
    x_s = (x // 3) * 3
    y_s = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            x = x_s + i
            y = y_s + i
            if board[x][y] == num:
                return False
            
    # Current number works for given location.
    return True

# Driver function for Sudoku.
def main():
    global board
    
    # Start with location on board.
    for x in range(9):
        for y in range(9):
            # Check if location is empty.
            if board[x][y] == 0:
                # Check if number in range from 1 to 10 is a valid choice. Backtrack if invalid.
                for num in range(1,10):
                    if validation(x, y, num):
                        board[x][y]  = num
                        main()
                        board[x][y] = 0
                return
        
    print(np.matrix(board))
    exit()

if __name__ == '__main__':
    main()