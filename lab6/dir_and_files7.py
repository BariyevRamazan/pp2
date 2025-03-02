with open("C:/Users/brama/Новая папка/.vscode/labs/lab6/Roskolnikov.txt", "r" ) as file:
    with open("Copy.txt", "w" ) as ofile:
        for i in file :
            ofile.write(i)
