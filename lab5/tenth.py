import re

text = input()
a = re.sub(r"[A-Z]", lambda x: "_" + x.group().lower(), text)
print(a)