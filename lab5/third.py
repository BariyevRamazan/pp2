import re

text = input()
pattern = r"[a-z]+_[a-z]+"
print(re.findall(pattern, text))