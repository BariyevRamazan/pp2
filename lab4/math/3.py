import math
n=int(input("sides num: "))
l=int(input("length of side: "))
p=l*n
a=l/(2*math.tan(math.radians(180/n)))
s=p*a/2
print(s)