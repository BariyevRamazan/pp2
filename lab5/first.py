import re
text = input()
pattern = r"ab*" 
result = re.fullmatch(pattern, text) 
if result != None:
    print("Right")
else:
    print("Not right")