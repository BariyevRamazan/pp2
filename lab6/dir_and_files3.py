import os
x = "C:/Users/brama/Новая папка/.vscode/labs/lab3/function2"
if os.access(x, os.F_OK):
    directory = os.path.dirname(x)
    filename = os.path.basename(x)
    print(f"Directory: {directory} \nFilename: {filename}")
else:
    print("Path doesn't exist")