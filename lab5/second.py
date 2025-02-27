import re

text = input()
pattern = r"a+[b]{2,3}"
result = re.fullmatch(pattern, text) 
if result != None :
    print("Matches")
else:
    print("Not matches")