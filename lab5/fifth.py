import re
text = input()
pattern = r"a.*b$"
a = re.fullmatch(pattern,text)
if a != None:
    print("True")
else:
    print("False")