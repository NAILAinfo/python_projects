file = input("enter the filename to open or create : ")
with open(file, "r") as f:
    contenu = f.read()

if contenu == "":
    print(file + "not found . Creating a new file .")
    create 
    print("enter your text (type 'SAVE' on a new line to save and exit) : ")


else:
    print("file found !")

try:
    with open("nouveau.txt", "x") as f:
        print(file + "not found . Creating a new file .")
        print("enter your text (type 'SAVE' on a new line to save and exit) : ")
        while True:
        p = input("")
        f.write(p)
        if phrase == "SAVE":
            print("File saved")
            break
except FileExistsError:
    print("file found !")
