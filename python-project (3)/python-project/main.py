
def print_grid(grid):
    print("\nSolved Sudoku Puzzle:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        row = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row.append("|")
            row.append(str(grid[i][j]))

        print(" ".join(row))


def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid(grid, num, row, col):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # Backtrack if the number does not work
            grid[row][col] = 0

    return False


# 0 represents an empty cell
grid = [
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

print("Original Sudoku Puzzle:")
print_grid(grid)

if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists for this Sudoku puzzle.")
