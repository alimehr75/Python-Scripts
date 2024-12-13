# Checking for repeated values.
def check_repeat(temp: list) -> bool:
    return len(temp) == len(set(temp))


# Checking for invalid values.
def check_1_9(temp: list) -> bool:
    for i in temp:
        if not 0 < int(i) <= 9:
            return False
    return True


# Remove non number items.
def remove_dot(temp: list) -> list:
    return list(filter(lambda x: x != ".", temp))


# Checking a rows validation.
def valid_row(row: int, board: list[list[str]]) -> bool:
    temp_row = board[row]
    return check_repeat(remove_dot(temp_row)) and check_1_9(remove_dot(temp_row))


# Checking a columns validation.
def valid_col(col: int, board: list[list[str]]) -> bool:
    # Extracting the column.
    temp_column = [row[col] for row in board]
    return check_repeat(remove_dot(temp_column)) and check_1_9(remove_dot(temp_column))


#  Checking validation of sub_squares 3*3.
def valid_sub(board: list[list[str]]) -> bool:
    sub_valid = True
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            temp_sub = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if board[r][c] != ".":
                        temp_sub.append(board[r][c])
            sub_valid &= check_repeat(temp_sub) and check_1_9(temp_sub)
    return sub_valid


#  Checking all board validation.
def valid_board(board: list[list[str]]) -> bool:
    row_valid = True
    column_valid = True
    for i in range(9):
        row_valid &= valid_row(i, board)
        column_valid &= valid_col(i, board)
    return row_valid and column_valid and valid_sub(board)

# Examples of boards

# board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#           [".", "9", "8", ".", ".", ".", ".", "6", "."],
#           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#           [".", "6", ".", ".", ".", ".", "2", "8", "."],
#           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#           [".", ".", ".", ".", "8", ".", ".", "7", "9"]] # --> Expect to be True
#
#
# print(valid_board(board1))
#
# board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
#           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#           [".", "9", "8", ".", ".", ".", ".", "6", "."],
#           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#           [".", "6", ".", ".", ".", ".", "2", "8", "."],
#           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]  # --> Expect to be False
#
# print(valid_board(board2))
#
# board3 = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
#           [".", "4", ".", "3", ".", ".", ".", ".", "."],
#           [".", ".", ".", ".", ".", "3", ".", ".", "1"],
#           ["8", ".", ".", ".", ".", ".", ".", "2", "."],
#           [".", ".", "2", ".", "7", ".", ".", ".", "."],
#           [".", "1", "5", ".", ".", ".", ".", ".", "."],
#           [".", ".", ".", ".", ".", "2", ".", ".", "."],
#           [".", "2", ".", "9", ".", ".", ".", ".", "."],
#           [".", ".", "4", ".", ".", ".", ".", ".", "."]]  # --> Expect to be False
#
# print(valid_board(board3))
