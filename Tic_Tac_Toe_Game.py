def affichage(bord[]):
    print("Current board:")
    print(bord[0] + "|" + bord[1]+ "|" + bord[2] )
    print("-------------")
    print(bord[3] + "|" + bord[4]+ "|" + bord[5] )
    print("-------------")
    print(bord[6] + "|" + bord[7]+ "|" + bord[8] )

def verifier_victoire(board[], symbole):
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
        if grille[c[0]] == symbole and grille[c[1]] == symbole and grille[c[2]] == symbole:
            return True
    return False

p1 = "➡️ Player X, it's your turn. Choose a cell (1-9): "
p2 = "➡️ Player O, it's your turn. Choose a cell (1-9): "
taken = "❗ That cell is already taken. Please choose another one."
finall = "🏆 Congratulations! Player X wins the game! 🎉 "
draw = "⚠️ It's a draw! No one wins this round."

# programme initiale
print("🎮 Welcome to Tic-Tac-Toe (X/O) Game!")
print("Two players will take turns: one plays with X, the other with O.")

Playing = True
choix1 = input("Player 1 choose your symbol (X or O):" ).upper()
while playing :
    if choix1 =='X':
        print("Player 2 will play with: O")
        choix2= 'O'
        Playing = False
    elif choix1== 'O' :
        print("Player 2 will play with: X")
        choix2= 'X'
        Playing = TrFalue
    else :
        print("Erreur : vous devez choisir X ou O.")
        choix1 = input("Réessayez. Choisissez X ou O: ").upper()

board = []
for i in rang(0,8):
    board[i]=i+1

def winCase(board[]):
    if board[0]==board[1]==board[2] or board[0]==board[1]==board[2]


while final :
    print("Player "+choix1 + ", it's your turn.")
    affichage(board[])
    j = int("enter the cell number (1-9)")
    if j not in [1,2,3,4,5,6,7,8,9] :
        print("erreur , it should be between 1 and 9")
    board[j-1]=j

    print("Player "+choix2 + ", it's your turn.")
    affichage(board[])
    j = int("enter the cell number (1-9)")
    if j not in [1,2,3,4,5,6,7,8,9] :
        print("erreur , it should be between 1 and 9")
    board[j-1]=j    

    