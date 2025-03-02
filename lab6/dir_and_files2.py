import os
raskolnikov = "C:/Users/brama/Новая папка/.vscode/labs/lab3/function2"
print("existence: ", end="")
if os.access(raskolnikov, os.F_OK):
    print("True")
else:
    print("False")
print("readability: ", end="")
if os.access(raskolnikov, os.R_OK):
    print("True")
else:
    print("False")
print("writability: ", end="")
if os.access(raskolnikov, os.W_OK):
    print("True")
else:
    print("False")
print("executability: ", end="")
if os.access(raskolnikov, os.EX_OK):
    print("True")
else:
    print("False")
