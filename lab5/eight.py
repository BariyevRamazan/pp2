import re

text = input()
a = re.split(r"[A-Z]",text)
print(a)