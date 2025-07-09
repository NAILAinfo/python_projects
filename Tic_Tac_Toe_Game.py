valeur = ['X', 'O']
score = {
    'X': 0,
    'O': 0
}

def affichage(board):
    print("\nCurrent board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-------------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-------------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def verifier_victoire(board, symbole):
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    return any(all(board[i] == symbole for i in combo) for combo in combinaisons)

def encore(board):
    return any(cell not in valeur for cell in board)

print("🎮 Welcome to Tic-Tac-Toe (X/O) Game!")
print("Two players will take turns: one plays with X, the other with O.")

choix1 = input("Player 1, choose your symbol (X or O): ").upper()
while choix1 not in valeur:
    print("❗ Error: you must choose X or O.")
    choix1 = input("Try again. Choose X or O: ").upper()

choix2 = 'O' if choix1 == 'X' else 'X'
print(f"Player 2 will play with: {choix2}")

playing = True
while playing:
    r = input('Do you want to play? (y/n): ').lower()
    if r == 'y':
        board = [str(i + 1) for i in range(9)]
        final = True
        actuel = choix1

        while final:
            affichage(board)
            try:
                j = int(input(f"Player {actuel}, choose a cell (1-9): "))
            except ValueError:
                print("❗ Invalid input. Please enter a number between 1 and 9.")
                continue

            if j < 1 or j > 9:
                print("❗ Error: number must be between 1 and 9.")
                continue

            if board[j - 1] in valeur:
                print("❗ That cell is already taken. Please choose another one.")
                continue

            board[j - 1] = actuel

            if verifier_victoire(board, actuel):
                affichage(board)
                print(f"🏆 Congratulations! Player {actuel} wins the game! 🎉")
                score[actuel] += 1
                break

            if not encore(board):
                affichage(board)
                print("⚠️ It's a draw! No one wins this round.")
                break

            actuel = choix2 if actuel == choix1 else choix1

    elif r == 'n':
        print("\nThanks for playing!")
        print("🏁 Final scores:")
        print(f"Player {choix1}: {score[choix1]}")
        print(f"Player {choix2}: {score[choix2]}")
        playing = False
    else:
        print("❗ Invalid input. Please enter 'y' or 'n'.")
