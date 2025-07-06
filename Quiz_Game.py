questions = {
        "q1": {
                    "question": "Quelle affirmation est correcte concernant une base de données relationnelle ?",
                            "choix": [
                                            "A. Chaque relation doit obligatoirement contenir une clé étrangère",
                                                        "B. Une relation est représentée par une table composée de lignes et de colonnes",
                                                                    "C. Une relation peut contenir des données non structurées comme des vidéos ou images sans contraintes",
                                                                                "D. Une relation ne peut jamais être vide"
                            ],
                                    "bonne_reponse": "B",
                                            "categorie": "BDD",
                                                    "difficulte": "A"
        },

            "q2": {
                        "question": "Quelle commande SQL permet de sélectionner toutes les colonnes d’une table appelée utilisateurs ?",
                                "choix": [
                                                "A. SELECT utilisateurs FROM *;",
                                                            "B. SELECT * FROM utilisateurs;",
                                                                        "C. GET * FROM utilisateurs;",
                                                                                    "D. CHOOSE ALL FROM utilisateurs;"
                                ],
                                        "bonne_reponse": "B",
                                                "categorie": "BDD",
                                                        "difficulte": "A"
            },

                "q3": {
                            "question": "Quelle est la fonction principale d’une clé primaire dans une table ?",
                                    "choix": [
                                                    "A. Permet de trier automatiquement les données",
                                                                "B. Autorise les doublons dans une table",
                                                                            "C. Permet de trier automatiquement les données",
                                                                                        "D. Identifie de manière unique chaque enregistrement"
                                    ],
                                            "bonne_reponse": "D",
                                                    "categorie": "BDD",
                                                            "difficulte": "A"
                },

                    "q4": {
                                "question": "Quel est le but d’une attaque de type phishing ?",
                                        "choix": [
                                                        "A. Détruire les serveurs de l’entreprise ciblée",
                                                                    "B. Voler des informations personnelles en se faisant passer pour un site ou un service fiable",
                                                                                "C. Tester la vitesse d’un réseau sécurisé",
                                                                                            "D. Détecter les vulnérabilités d’un système via des tests automatisés"
                                        ],
                                                "bonne_reponse": "B",
                                                        "categorie": "SEC",
                                                                "difficulte": "A"
                    },

                        "q5": {
                                    "question": "Quel protocole est utilisé pour sécuriser les communications sur un site web ?",
                                            "choix": [
                                                            "A. HTTP",
                                                                        "B. FTP",
                                                                                    "C. HTTPS",
                                                                                                "D. SMTP"
                                            ],
                                                    "bonne_reponse": "C",
                                                            "categorie": "SEC",
                                                                    "difficulte": "A"
                        },

                            "q6": {
                                        "question": "Quel est le mot de passe le plus sécurisé parmi les suivants ?",
                                                "choix": [
                                                                "A. 123456",
                                                                            "B. password",
                                                                                        "C. Jean2020",
                                                                                                    "D. A9@l$8xQ#7!"
                                                ],
                                                        "bonne_reponse": "D",
                                                                "categorie": "SEC",
                                                                        "difficulte": "A"
                            },

                                "q7": {
                                            "question": "Quel domaine de l’IA consiste à apprendre à partir de données ?",
                                                    "choix": [
                                                                    "A. Vision par ordinateur",
                                                                                "B. Apprentissage automatique",
                                                                                            "C. Robotique",
                                                                                                        "D. Traitement du signal"
                                                    ],
                                                            "bonne_reponse": "B",
                                                                    "categorie": "IA",
                                                                            "difficulte": "A"
                                },

                                    "q8": {
                                                "question": "Quel langage est souvent utilisé pour développer des algorithmes d’IA ?",
                                                        "choix": [
                                                                        "A. HTML",
                                                                                    "B. CSS",
                                                                                                "C. Python",
                                                                                                            "D. SQL"
                                                        ],
                                                                "bonne_reponse": "C",
                                                                        "categorie": "IA",
                                                                                "difficulte": "A"
                                    },

                                        "q9": {
                                                    "question": "Quel système d’exploitation est basé sur le noyau Linux ?",
                                                            "choix": [
                                                                            "A. Windows",
                                                                                        "B. macOS",
                                                                                                    "C. Ubuntu",
                                                                                                                "D. MS-DOS"
                                                            ],
                                                                    "bonne_reponse": "C",
                                                                            "categorie": "OS",
                                                                                    "difficulte": "A"
                                        },

                                            "q10": {
                                                        "question": "Quel est le rôle principal d’un système d’exploitation ?",
                                                                "choix": [
                                                                                "A. Créer des documents",
                                                                                            "B. Fournir un environnement pour exécuter des logiciels",
                                                                                                        "C. Protéger contre les virus",
                                                                                                                    "D. Stocker les vidéos"
                                                                ],
                                                                        "bonne_reponse": "B",
                                                                                "categorie": "OS",
                                                                                        "difficulte": "A"
                                            }
}

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