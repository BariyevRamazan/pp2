import os
x = "C:/Users/brama/Новая папка/.vscode/labs/lab6/last_exercise.txt"
if os.access(x, os.F_OK):
    os.remove(x)
    print(f"x '{x}' deleted successfully")
else:
    print("x doesn't exist")