import string

for i in string.ascii_uppercase:
    filename = f"{i}.txt" 
    with open(filename, "w") as file:
        file.write("My name is Ramazan")

