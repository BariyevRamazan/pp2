import re

text = input()
a = re.sub(r"[A-Z]", lambda x: " " + x.group(), text)
print(a)
