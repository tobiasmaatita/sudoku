import time 
from datetime import timedelta

def string_to_board(file, i=0):
    """Convert the input string into a 9x9 2D list."""
    with open(file, 'r') as f:
        sudoku_string = [s.strip() for s in f.readlines()][i]
    return [[int(sudoku_string[i*9 + j]) for j in range(9)] for i in range(9)]

def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i, row in enumerate(board):
        print_row = ""
        if i in [3, 6]:
            print('------+-------+------')
        for j, value in enumerate(row):
            if value == 0 : value = "."
            if j in [3, 6]:
                print_row += " | "
            if j in [2, 5]:
                print_row += str(value)
            else:
                print_row += f"{value} "
        print(print_row)

def is_valid(board, row, col, num):
    """Check if it's valid to place the number `num` at board[row][col]."""
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell found
                for num in range(1, 10):  # Try digits 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        solved, solution = solve_sudoku(board)
                        if solved:
                            return True, solution
                        board[row][col] = 0  # Backtrack
                return False, None  # Trigger backtracking
    return True, board  # All cells are filled correctly

def time_passed(start_time):
    end_time = time.time()
    passed = end_time - end_time
    print(timedelta(milliseconds=passed))

if __name__ == "__main__":
    start = time.time()
    board = string_to_board("nyt.txt")
    print("Input board:")
    print_board(board)
    print()
    solved, solution = solve_sudoku(board)
    if solved:
        print("Done! Solution:")
        print_board(solution)
        