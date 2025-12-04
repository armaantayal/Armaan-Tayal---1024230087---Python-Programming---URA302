# Tic-Tac-Toe Game – Project 1
def create_board():
    return [" "]*9

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def check_tie(board):
    return all(cell != " " for cell in board)

def get_player_input(player, board):
    while True:
        pos = input(f"Player {player}, enter position (1-9): ")
        if not pos.isdigit():
            print("Enter a number 1-9.")
            continue
        pos = int(pos)
        if pos < 1 or pos > 9:
            print("Position must be between 1 and 9.")
            continue
        idx = pos - 1
        if board[idx] != " ":
            print("Position already taken.")
            continue
        return idx

def play_game():
    board = create_board()
    current_player = "X"
    while True:
        print_board(board)
        move = get_player_input(current_player, board)
        board[move] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
