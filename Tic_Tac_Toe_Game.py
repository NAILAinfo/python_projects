valeur = ['X','O']
def affichage(bord):
    print("Current board:")
    print(bord[0] + "|" + bord[1]+ "|" + bord[2] )
    print("-------------")
    print(bord[3] + "|" + bord[4]+ "|" + bord[5] )
    print("-------------")
    print(bord[6] + "|" + bord[7]+ "|" + bord[8] )

def verifier_victoire(board, symbole):
    combinaisons = [
        [0, 1, 2],  # ligne 1
        [3, 4, 5],  # ligne 2
        [6, 7, 8],  # ligne 3
        [0, 3, 6],  # colonne 1
        [1, 4, 7],  # colonne 2
        [2, 5, 8],  # colonne 3
        [0, 4, 8],  # diagonale \
        [2, 4, 6]   # diagonale /
    ]
    for c in combinaisons:
        if board[c[0]] == symbole and board[c[1]] == symbole and board[c[2]] == symbole:
            return True
    return False

def encore(board):
    for i in range(9):
        if board[i] == i + 1:
            return True  
    return False  

print("🎮 Welcome to Tic-Tac-Toe (X/O) Game!")
print("Two players will take turns: one plays with X, the other with O.")

choix1 = input("Player 1 choose your symbol (X or O):" ).upper()
while choix1 not in valeur] :
    print("Erreur : vous devez choisir X ou O.")
    choix1 = input("Réessayez. Choisissez X ou O: ").upper()

choix2 = 'O' if choix1=='X' else 'X'
print(f"Player 2 will play with: {choix2}")



board = []
for i in range(0,8):
    board[i]=i+1

final =True
actuel= choix1


while final :
    affichage(board)
    j = int(input("Player "+ actuel + ", it's your turn. Choose a cell (1-9): "))
    if j< 1 or j > 9: :
        print("erreur , it should be between 1 and 9")
        continue

    if board[j-1] in valeur :
        print("❗ That cell is already taken. Please choose another one.")
        continue
    
    board[j-1]= actuel

    if verifier_victoire(board, actuel):
        print("🏆 Congratulations! Player "+ actuel + " wins the game! 🎉" )
        print('Thanks for playing!')
        break

    if not encore(board)  :
        affichage(board)
        print( "⚠️ It's a draw! No one wins this round.")
        break

    actuel = choix2 if actuel ==choix1 else choix1    