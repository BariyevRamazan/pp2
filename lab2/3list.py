tlist=[1,2,3,4]
print(tlist)
print("len =", len(tlist))
tlist=[False,12,"vefe",1j] #IT WORKS!!!
print(tlist)
tlist=list((1,2,3,23,5,74,56))
print(tlist)

#Access Items
print(tlist[0])
print(tlist[-1])
print(tlist[1:7])
print(tlist[:3])
print(tlist[5:])

#Change Item Value
l=[8,1,4,8]
l[0]=l[1]
print(l)
l[1:3]=[4]
print(l)
l.insert(0,1)
print(l)

#Add List Items
l.append(5)
print(l)
l2=(1,9,1)
l.extend(l2)
print(l)

#Remove List Items
l.remove(1)
print(l)
l.pop(1)
print(l)
l.pop() #last element
print(l)
del l[2]
print(l)
del l
l=[1,2,9]
l.clear()
l.append(5)
l.append(1)
l.append(2)
print(l)
#Loop Lists
for it in l:
    print(it)

for i in range(len(l)):
    print(l[i])

j=0
while j<len(l):
    print(l[j])
    j+=1

[print(x) for x in l]

#List Comprehension
lo=["ggg","rtp","gik","hola","gel"]
n=[]
for i in range(len(lo)):
    if "g" in lo[i]:
        n.append(lo[i])
print(n)

ni=[x for x in lo if "l" in x]
print(ni)
no=[x for x in range(10)]
print(no)
kl=[x.upper() for x in lo]
print(kl)
upi=[x if x!="ggg" else "Alv" for x in lo]
print(upi)
