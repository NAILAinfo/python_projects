import csv 
 

listt = []
# le task est definie par nom , categorie 
# le task peut etre modifier , supprimer , ajouter , completed , filter by categories
# save the liste to a flie  and loads it when the program starts
task = {
    'name'= 

}


print(listt.values())
 
def menu():
    print("Todo List Menu :")
    print("1.View tasks")
    print("2.Add a Task")
    print("3.Remove a Task")
    print("4.Exit")

def choice(): 
    valide = False    
    while not valide :
        i = int(input("Enter your choice :"))
        if 1 <= i <= 4:
                valide = True
            else:
                print("Erreur : le nombre doit être entre 1 et 4.")
    return i

def ajouter():
    y = input("Enter the categorie of the task :")
    x = input("Enter a new task :")
    newTask = {"categorie" : y ,"task": x ,"etat":false}
    listt.append(newTask)

def supprimer():    
    x = input("Enter the task tha you want to remove :")
    listt = [e for e in listt if e["task"] != x]

def affichageAll():
    print("------------------------------------------------------------------")
    print("|    Tasks                   |   Catgorie      |     Statue     | ")
    for e in listt :
        print("|" ,e["task"],"|" ,e["categorie"] "|"  , e["etat"] )
        print("---------------------------------------------------------------")


def affichageDid