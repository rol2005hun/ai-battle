def is_valid(board, row, col, num):
    """Check if placing `num` at (row, col) is valid."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack if invalid
                return False  # Trigger backtracking
    return True  # Puzzle solved

def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Example Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve and print the Sudoku board
print("Initial Sudoku Board:")
print_board(sudoku_board)
print("\nSolving...\n")

if solve_sudoku(sudoku_board):
    print("Solved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("No solution exists.")