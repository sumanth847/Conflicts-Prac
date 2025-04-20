import random

# A sample board with some pre-filled values (0 = empty)
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

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def is_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def sudoku_game():
    print("Welcome to Sudoku!")
    while not is_full(sudoku_board):
        print_board(sudoku_board)
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter col (0-8): "))
            num = int(input("Enter number (1-9): "))
            if sudoku_board[row][col] != 0:
                print("Cell is already filled. Try another one.")
                continue
            if is_valid(sudoku_board, row, col, num):
                sudoku_board[row][col] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter valid numbers.")
        except IndexError:
            print("Row and column must be between 0 and 8.")
    print_board(sudoku_board)
    print("Congratulations! You've completed the Sudoku puzzle.")

if __name__ == "__main__":
    sudoku_game()
