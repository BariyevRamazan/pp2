# Sort Lists
p=['c','d','a','e','b']
p.sort()
print(p)
p=[5,2,6,4,3,9]
p.sort()
print(p)
p.reverse()
print(p)
p=[1,2,3,8,5,1,65]
p.sort(reverse=True)
print(p)

def g(n):
    return abs(n-30)
o=[45,69,32,12,79]
o.sort(key=g)
print(o)
o=["ab","Ab","lb","Pb","Rb","bb"]
o.sort(key=str.lower)
print(o)
thislist = ["banana", "Orange", "Aiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Copy Lists
r=o.copy()
print(r)
r=p[:]
print(p)

#Join Lists
k=o+p
print(k)

for x in o:
    p.append(x)
print(p)

c=[1,2,3]
o.extend(c)
print(o)