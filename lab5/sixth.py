import re
text = input()
pattern = r"[., ]"
a = re.sub(pattern,":",text)
print(a)