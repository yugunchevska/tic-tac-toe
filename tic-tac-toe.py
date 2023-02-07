board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    choice = int(input("Enter your move, {} (1-9): ".format(icon)).strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print("That space is taken")

def is_row_victory(icon, board_slice):  
    for cell in board_slice:
        if cell != icon:
            return False
    return True

def is_victory(icon):
    if is_row_victory(icon, board[0:3]) or \
       is_row_victory(icon, board[3:6]) or \
       is_row_victory(icon, board[6:9]) or \
       is_row_victory(icon, board[0:7:3]) or \
       is_row_victory(icon, board[1:8:3]) or \
       is_row_victory(icon, board[2:9:3]) or \
       is_row_victory(icon, board[0:9:4]) or \
       is_row_victory(icon, board[2:7:2]):
        return True
    return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("Z")
    if is_victory("Z"):
        print("Z wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break
