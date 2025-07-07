import csv 
📥 Lire le fichier CSV

🧠 Stocker les données dans une structure (liste de dictionnaires par exemple)

❓ Afficher les questions une à une

✅ Comparer la réponse de l’utilisateur avec la bonne réponse

🧾 Afficher le score final

questions = []

with open('quiz_game .csv', newline='', encoding='utf-8') as file:
    lecteur = csv.DictReader(file)
    for ligne in lecteur:
        question = dict('question'=)



print('Bienvenue dans le quiz !')

print('Choisis une catégorie pour commencer :')
print('1.🤖 Intelligence Artificielle (IA)')
print('2.🖥️ Systèmes d’exploitation (OS)')
print('3.🔐 Cybersécurité')
print('4.🗃️Base de donnees ')

ctg = {'1':'IA' , '2':'OS' , '3':'SEC' , '4':'BDD'}
c=0
choix = int(input(':')
if choix not in ctg:
        print('le numero doit etre soit 1 , 2 , 3')
        else :
                choix = ctg[choix]
                    print('Choisis le niveau de difficulte :')
                        print('1.Debutant')
                            print('2.Intermédiaire ')
                                print('3.Avance ')
                                
                                    level = int(input(':')
                                        if level not in ['1','2','3'] :
                                                   print('le numero doit etre  1 , 2 ou 3')
                                                       else :
                                                                print('Le quiz va commencer, bonne chance ! ')
                                                                        for e in questions.values():
                                                                                        if e["categories"]==choix :
                                                                                                            print(e["question"]+"?")
                                                                                                                            for c in e["choix"]:
                                                                                                                                                    print(c)
                                                                                                                                                                    x = input("votre reponse :")
                                                                                                                                                                                    if x not in ['A','B','C','D']:
                                                                                                                                                                                                            print('la reponse doit etre A , B , C ou D')
                                                                                                                                                                                                                            else :
                                                                                                                                                                                                                                                    if e["bonne_reponse"] == x:   
                                                                                                                                                                                                                                                                                    print("bonne reponse ")
                                                                                                                                                                                                                                                                                                                c+=1
                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                print("c'est faux ")
                                                                                                                                                                                                                                                                                                                                                                print(f"ton score finale est :{c}")))
                                                                ]
                                            }
                                                            ]
                                        }
                                                        ]
                                    }
                                                    ]
                                }
                                                ]
                            }
                                            ]
                        }
                                        ]
                    }
                                    ]
                }
                                ]
            }
                            ]
        }
}