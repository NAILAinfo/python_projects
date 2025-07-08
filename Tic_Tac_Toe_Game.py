player1 = input("nom du premier joueur")
player2 = input("nom du deuxieme joueur")

choix1 = input(player1 , "choisit-tu de jouer avec X ou bien O ")
if choix1 =='X':
    print("geniale , donc" , player2 , "va jouer avec O")
    choix2= 'O'
elif choix1== 'O' :
    print("geniale , donc" , player2 , "va jouer avec X")
    choix2= 'X'
else :
    print("Entrée invalide. Choisissez X ou O")

