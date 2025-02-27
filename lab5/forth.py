import re
text = input()
pattern = r"[A-Z]+_[a-z]{2,}"
a = re.findall(pattern,text)
if not a:
    print("There is no string with matches to pattern")
else:
    print(a)
