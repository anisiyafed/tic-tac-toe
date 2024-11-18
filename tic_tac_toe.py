print("Welcome to Tic-Tac-Toe")
print("Player 1 is 'X' and Player 2 is 'O'")

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def is_draw():
    # Draw if no moves left
    for spot in board:
        if spot not in ["X", "O"]:
            return False
    return True

print_board()
current_player = "X"

while True:
    try:
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        if move < 0 or move >= 9 or board[move] in ["X", "O"]:
            print("Invalid move. Try again.")
            continue
    except ValueError:
        print("Please enter a number between 1 and 9.")
        continue

    board[move] = current_player
    
    print_board()

    if check_winner(current_player):
        print(f"Player {current_player} wins!")
        break

    if is_draw():
        print("It's a draw!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"






