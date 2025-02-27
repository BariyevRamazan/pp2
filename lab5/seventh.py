import re

text = input()
a = re.split(r"_",text)
result=""
i=0
for x in a:
    if i != 0 :
        x = x.capitalize()
    result += x
    i+=1
print(result)