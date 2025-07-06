import random

historique = []

def game(p):
    emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
    
    if p == 1:
        s = input('Rock, paper or scissors? (r/p/s): ').lower()
        if s not in emojis:
            print('Invalid choice. Please choose r, p, or s.')
            return None
        print('You chose:', emojis[s])
        computer_choice = random.choice(['r', 'p', 's'])
        print('Computer chose:', emojis[computer_choice])
        
        if s == computer_choice:
            print("It's a tie!")
            historique.append([s, computer_choice, 'égalité'])
            return None
        elif (s == 'r' and computer_choice == 's') or \
             (s == 'p' and computer_choice == 'r') or \
             (s == 's' and computer_choice == 'p'):
            print("You win this round!")
            historique.append([s, computer_choice, 'joueur'])
            return "player1"
        else:
            print("Computer wins this round!")
            historique.append([s, computer_choice, 'ordinateur'])
            return "player2"
    
    elif p == 2:
        s1 = input('Player 1, rock, paper or scissors? (r/p/s): ').lower()
        s2 = input('Player 2, rock, paper or scissors? (r/p/s): ').lower()
        if s1 not in emojis or s2 not in emojis:
            print('Invalid choice. Please choose r, p, or s.')
            return None
        print('Player 1 chose:', emojis[s1])
        print('Player 2 chose:', emojis[s2])
        
        if s1 == s2:
            print("It's a tie!")
            historique.append([s1, s2, 'égalité'])
            return None
        elif (s1 == 'r' and s2 == 's') or \
             (s1 == 'p' and s2 == 'r') or \
             (s1 == 's' and s2 == 'p'):
            print("Player 1 wins this round!")
            historique.append([s1, s2, 'joueur 1'])
            return "player1"
        else:
            print("Player 2 wins this round!")
            historique.append([s1, s2, 'joueur 2'])
            return "player2"

def play(p):
    player1_score = 0
    player2_score = 0

    while player1_score < 2 and player2_score < 2:
        winner = game(p)
        if winner == "player1":
            player1_score += 1
        elif winner == "player2":
            player2_score += 1
    affiche_resultat(player1_score, player2_score, p)

def affiche_resultat(player1_score, player2_score, p):
    print("Score :") 
    if p == 1:
        print(f"Final Score: You: {player1_score} | Computer: {player2_score}")
        if player1_score == 2:
            print("🎉 You are the overall winner!\n")
        else:
            print("💻 The computer wins!\n")
    else:
        print(f"Final Score: Player 1: {player1_score} | Player 2: {player2_score}") 
        if player1_score == 2:
            print("🎉 Player 1 is the winner!\n")
        else:
            print("🎉 Player 2 is the winner!\n")

def affiche_historique(p):
    print("📜 Historique des parties :")
    if p == 1:
        for i, entry in enumerate(historique, 1):
            print(f"Manche {i} : Joueur: {entry[0]}, Ordinateur: {entry[1]}, Gagnant: {entry[2]}")
    else:
        for i, entry in enumerate(historique, 1):
            print(f"Manche {i} : Joueur 1: {entry[0]}, Joueur 2: {entry[1]}, Gagnant: {entry[2]}")

# Choix du mode de jeu
p = int(input("Do you want to play against the computer (1) or against another player (2)? "))

if p in [1, 2]:
    while True:
        play(p)
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            affiche_historique(p)
            break
else:
    print("Invalid choice. Please choose 1 or 2.")
 