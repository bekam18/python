import random
import os
import time

# Game board generator
def create_board(size):
    symbols = [chr(65 + i) for i in range(size * size // 2)] * 2  # Create pairs of symbols (A, B, C...)
    random.shuffle(symbols)
    return [symbols[i:i+size] for i in range(0, len(symbols), size)]

# Display the current state of the board
def display_board(board, revealed):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print("Memory Game Board\n")
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if revealed[i][j]:
                row_display.append(cell)
            else:
                row_display.append("X")
        print(" ".join(row_display))
    print("\n")

# Check if all cells are revealed
def all_revealed(revealed):
    return all(all(row) for row in revealed)

# Main game function
def memory_game():
    size = 4  # Board size: 4x4
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]

    moves = 0
    pairs_found = 0

    while not all_revealed(revealed):
        display_board(board, revealed)
        
        try:
            print("Enter the coordinates (row and column) of the first card:")
            r1, c1 = map(int, input("Row Col (0-indexed): ").split())
            print("Enter the coordinates of the second card:")
            r2, c2 = map(int, input("Row Col (0-indexed): ").split())

            # Validate inputs
            if not (0 <= r1 < size and 0 <= c1 < size and 0 <= r2 < size and 0 <= c2 < size):
                print("Invalid coordinates! Try again.")
                time.sleep(1)
                continue

            if revealed[r1][c1] or revealed[r2][c2] or (r1 == r2 and c1 == c2):
                print("Invalid move! Try again.")
                time.sleep(1)
                continue
            
            # Reveal cards
            revealed[r1][c1], revealed[r2][c2] = True, True
            display_board(board, revealed)
            moves += 1

            # Check for a match
            if board[r1][c1] == board[r2][c2]:
                print("It's a match!")
                pairs_found += 1
            else:
                print("Not a match. Cards will flip back.")
                revealed[r1][c1], revealed[r2][c2] = False, False
                time.sleep(2)

        except ValueError:
            print("Invalid input format. Please enter row and column as numbers.")
            time.sleep(1)

    print(f"Congratulations! You found all pairs in {moves} moves.")

# Run the game
if __name__ == "__main__":
    memory_game()
