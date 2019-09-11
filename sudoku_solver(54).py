import numpy as np
sudoku_board_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_board_2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]]

# Function to extract values in a row as a list
def extract_row_values(board, row):
    return board[row]

# Function to extract column values as a list
def extract_col_values(board, col):
    return [board[i][col] for i in range(0, 9)]

# Function to extract values in a 3 * 3 grid as a list
def extract_grid(board, row, col):
    row_first = (row // 3) * 3
    col_first = (col // 3) * 3
    return [board[row_first + i][col_first + j] for i in range(0,3) for j in range(0, 3)]

# Checking if final solution is reached
def check_final_solution(board):
    for i in range(0, 9):
        # If 0 still in board, final solution not reached. Plausibility Check
        if 0 in board[i]:
            return False

    for i in range(0, 9):
        # Checking the row and columns values for a sum of 45
        a = np.sum(extract_row_values(board, i))
        b = np.sum(extract_col_values(board, i))
        if a != 45 or b != 45:
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            # Checking all 3 * 3 grids for a sum of 45
            a = np.sum(extract_grid(board, i, j))
            if a != 45:
                return False

    return True

# Function to check possible values for an unfilled position
def sudoku_solver_list(board, row, col):
    row_list = extract_row_values(board, row)
    col_list = extract_col_values(board, col)
    grid_list = extract_grid(board, row, col)
    possible_val = []
    for i in range(1, 10): # Numbers from 1 to 9
        if i not in row_list and i not in col_list and i not in grid_list:
            possible_val.append(i)
    # List of possible values for an unfilled position
    return possible_val

# Generating a dictionary containing the unfilled positions(row, col) as keys and the possible values as 'values'
def sudoku_possible_val(board):
    pos_val = {}
    redo = False
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                possible_val = sudoku_solver_list(board, row, col)
                # Resolving it right here if only one possible values for an unfilled position
                if len(possible_val) == 1:
                    board[row][col] = possible_val[0]
                    # Updating the 'Possible value dictionary' to remove the updated value
                    for k in range(0, 9):
                        if (row, k) in pos_val and possible_val[0] in pos_val[(row, k)]:
                            pos_val[(row, k)].remove(possible_val[0])
                            redo = True
                        if (k, col) in pos_val and possible_val[0] in pos_val[(k, col)]:
                            pos_val[(k, col)].remove(possible_val[0])
                            redo = True
                else:
                    # Adding the (row, col) as a key in the dictionary
                    pos_val[(row, col)] = possible_val
    return board, pos_val, redo

def sudoku_solver_missing_val(row, col, pos_val):
    '''
    Function to create a list of lists for a particular unfilled position
    Row list consists of lists of all unfilled position in the same row
    Column list consists of lists of possible values for all unfilled positions in the same column
    Grid list consists of lists of possible values for all unfilled positions in the same 3 * 3 grid
    '''
    row_list = []
    col_list = []
    grid_list = []
    grid_pos = []
    row_pos = []
    col_pos = []

    for k in range(0, 9):
        if (row, k) in pos_val:
            row_list.append(pos_val[(row, k)])
            row_pos.append((row, k))
        if (k, col) in pos_val:
            col_list.append(pos_val[(k, col)])
            col_pos.append((k, col))

    row_val = (row // 3) * 3
    col_val = (col // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if (row_val + i, col_val + j) in pos_val:
                grid_list.append(pos_val[(row_val + i, col_val + j)])
                grid_pos.append((row_val + i, col_val + j))

    return row_list, row_pos, col_list, col_pos, grid_list, grid_pos

# Check if values can be filled. Update values if possible. Returns a list of (row, col) which were modified in the board
def fill_in_values(board, pos_list, rc_pos, pos_val):
    val_dict = {} # Dictionary to find out unique values that fill a position in the board
    ret = []
    for idx in range(0, len(pos_list)):
        for val in pos_list[idx]:
            if val in val_dict:
                val_dict[val].append(idx)
            else:
                val_dict.setdefault(val, [idx])

    for key in val_dict:
        if len(val_dict[key]) == 1:
            # Only one possible value
            r, c = rc_pos[val_dict[key][0]]
            board[r][c] = key
            ret.append((r, c))
    return board, ret, pos_val

# Sudoku Solver main function
def sudoku_solver(board):
    '''
    Finally the main function :P
    Checks for possible fill-able positions in the row, then in the column
    And finally checks the same in the 3 * 3 grid
    Updates the possible values as and when values are filled in the board
    Continues the function call until all positions are filled and all rows, columns and grid positions add up to 45
    1 + 2 + ... + 9 = (9)(10) / 2 = 45
    '''

    board, pos_val, redo = sudoku_possible_val(board)
    while redo == True:
        board, pos_val, redo = sudoku_possible_val(board)
    for (row, col) in list(pos_val):
        row_list, row_pos, col_list, col_pos, grid_list, grid_pos =  sudoku_solver_missing_val(row, col, pos_val)
        board, ret, pos_val = fill_in_values(board, row_list, row_pos, pos_val)

        if len(ret) != 0:
            for (r, c) in ret:
                pos_val.pop((r, c))
            board, pos_val, redo = sudoku_possible_val(board)
            row_list, row_pos, col_list, col_pos, grid_list, grid_pos = sudoku_solver_missing_val(row, col, pos_val)

        board, ret, pos_val = fill_in_values(board, col_list, col_pos, pos_val)

        if len(ret) != 0:
            for (r, c) in ret:
                pos_val.pop((r, c))
            board, pos_val, redo = sudoku_possible_val(board)
            row_list, row_pos, col_list, col_pos, grid_list, grid_pos = sudoku_solver_missing_val(row, col, pos_val)

        board, ret, pos_val = fill_in_values(board, grid_list, grid_pos, pos_val)

        if len(ret) != 0:
            for (r, c) in ret:
                pos_val.pop((r, c))
            board, pos_val, redo = sudoku_possible_val(board)

    retVal = check_final_solution(board)
    if retVal == False:
        board, pos_val = sudoku_solver(board)

    return board, pos_val


if __name__ == '__main__':
    board, pos_val = sudoku_solver(sudoku_board_2)
    print(np.array(board))
    print(check_final_solution(board))






