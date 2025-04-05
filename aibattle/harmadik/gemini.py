def find_empty(board):
    """Finds the first empty cell (0) in the board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Row, Col
    return None

def valid(board, num, pos):
    """Checks if placing 'num' at 'pos' is a valid move."""
    row, col = pos

    # Check row
    for i in range(9):
        if board[row][i] == num and (row, i) != pos:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and (i, col) != pos:
            return False

    # Check box (3x3 subgrid)
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3):
        for j in range(box_x * 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solves the Sudoku board using backtracking."""

    empty_pos = find_empty(board)
    if not empty_pos:
        return True  # Board is full, solution found

    row, col = empty_pos

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):  # Recursively try to solve
                return True

            board[row][col] = 0  # Backtrack: reset if no solution found

    return False  # No valid number found for this cell


def print_board(board):
    """Prints the Sudoku board in a user-friendly format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - -   - - -   - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            print(board[i][j], end=" ")

        print()

    if (i+1) % 3 == 0 and (i+1) != 0:
            print("- - -   - - -   - - -")



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

if solve(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")