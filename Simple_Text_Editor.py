filename = input("Enter the filename to open or create: ")

try:
    # Tente de créer un nouveau fichier
    with open(filename, "x") as f:
        print(f"{filename} not found. Creating a new file.")
        print("Enter your text (type 'SAVE' on a new line to save and exit):")
        while True:
            line = input(" ")
            if line == "SAVE":
                print("File saved.")
                break
            f.write(line + "\n")
except FileExistsError:
    print("File found!")

    # Choix entre overwrite ou append
    choice = input("Do you want to overwrite (O) or append (A) to the file? ").strip().upper()
    mode = "w" if choice == "O" else "a"

    with open(filename, mode) as f:
        print("Enter your text (type 'SAVE' on a new line to save and exit):")
        while True:
            line = input(" ")
            if line == "SAVE":
                print("Changes saved.")
                break
            f.write(line + "\n")

    # Option de recherche et remplacement
    replace_choice = input("Do you want to search and replace text? (yes/no): ").strip().lower()
    if replace_choice == "yes":
        search_text = input("Enter the word or phrase to search: ")
        replace_text = input("Enter the replacement: ")

        # Lire tout le contenu
        with open(filename, "r") as f:
            content = f.read()

        # Remplacer
        new_content = content.replace(search_text, replace_text)

        # Écraser avec le nouveau contenu
        with open(filename, "w") as f:
            f.write(new_content)

        print("Replacement completed and file updated.")
