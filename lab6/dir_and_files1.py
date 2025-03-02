import os
x = "C:/Users/brama/Новая папка/.vscode/labs/lab3/function2"
list_of_war = os.listdir(path=x)
print("only dir:")
for i in list_of_war:
    if os.path.isdir(f"{x}/{i}"):
        print(i)

print("only file:")
list_of_us = []
for i in list_of_war:
    if os.path.isfile(f"{x}/{i}"):
        list_of_us.append(i)
print(list_of_us)