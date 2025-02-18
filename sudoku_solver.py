# Solve Sudoku by taking input from user
import numpy as np
import time
import copy

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- " * 11)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            cell_value = board[row][col]
            print(cell_value if cell_value != 0 else " ", end=" ")
        print()

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None

def valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
    
if __name__ == "__main__":
    board = np.array([[0, 0, 0, 0, 9, 1, 0, 0, 0],
                    [0, 6, 0, 0, 0, 0, 5, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 2, 1],
                    [0, 8, 0, 6, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [1, 0, 9, 0, 0, 0, 0, 3, 0],
                    [4, 0, 0, 0, 5, 0, 6, 0, 0],
                    [0, 0, 0, 8, 0, 0, 0, 0, 0]])
    print_board(board)
    start = time.time()
    solve(board)
    end = time.time()
    print_board(board)
    print("Time taken: ", end - start)
    print("Total number of steps: ", board.sum())
    