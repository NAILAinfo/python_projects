import csv

def charger_questions(fichier_csv, categorie=None, difficulte=None):
    questions = []
    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (categorie and row["categorie"].lower() != categorie.lower()) or \
               (difficulte and row["difficulte"].lower() != difficulte.lower()):
                continue
            question = {
                "texte": row["question"],
                "choix": {
                    "A": row["choix1"],
                    "B": row["choix2"],
                    "C": row["choix3"],
                    "D": row["choix4"]
                },
                "bonne_reponse": row["bonne_reponse"].upper(),
                "categorie": row["categorie"],
                "difficulte": row["difficulte"]
            }
            questions.append(question)
    return questions

def jouer_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i} [{q['categorie']} - {q['difficulte'].capitalize()}]")
        print(q["texte"])
        for lettre, choix in q["choix"].items():
            print(f"{lettre}. {choix}")
        while True:
            reponse = input("Votre réponse (A, B, C ou D) : ").strip().upper()
            if reponse in ['A', 'B', 'C', 'D']:
                break
            print("Entrée invalide. Choisissez A, B, C ou D.")
        if reponse == q["bonne_reponse"]:
            print("Bonne réponse !")
            score += 1
        else:
            print(f"❌ Mauvaise réponse.")
            print(f"La bonne réponse était {q['bonne_reponse']}: {q['choix'][q['bonne_reponse']]}")
    print(f"\n🎯 Score final : {score} / {len(questions)}")

#  Programme principal 
if __name__ == "__main__":
    fichier = "questions.csv"

    ctgr = input("Filtrer par catégorie (laisser vide pour tout) : ").strip()
    diff = input("Filtrer par difficulté (débutant, intermediaire, avance, vide pour tout) : ").strip()

    if ctgr == "":
        ctgr = None
    if diff == "":
        diff = None

    questions = charger_questions(fichier, categorie=ctgr, difficulte=diff)
    if not questions:
        print("Aucune question trouvée avec ces filtres.")
    else:
        jouer_quiz(questions)

