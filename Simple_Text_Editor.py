file = input("enter the filename to open or create : ")
try:
    with open("nouveau.txt", "x") as f:
        print(file + "not found . Creating a new file .")
        print("Enter your text (type 'SAVE' on a new line to save and exit) : ")
        while True:
            p = input(" ")
            if p == "SAVE":
                print("File saved")
                break
            f.write(p +"\n" )
except FileExistsError:
    print("File found !")
