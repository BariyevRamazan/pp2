s={4,2,2,3,True,"rfgr"}
print(s)
m={"z","c","x"}
print(m)
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
print(type(s))
u=set((1,35,8,9,9))
print(u,1)

#acces
print(8 in u)

#add
u.add("vdv")
print(u)
u.update(s)
print(u)
l=["gtt",11,35]
u.update(l)
print(u)

#remove
u.discard(35)
print(u)

#Join
p={"g","l","j"}
p2={5,6,1}
p3=p.union(p2)
print(p3)
p4=p | p2
print(p4)
p5={"j",1,"k","ou",79}
p6=p.union(p2,p5)
print(p6)
p6.clear()
p6=p|p2|p5
print(p6)
set1= {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
set4=set1&set2
print(set4)
set1.intersection_update(set2)
print(set1)
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
set4=set1-set2
print(set4)
set1.difference_update(set2)
print(set1)
set1= {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.symmetric_difference(set2)
print(set3)
set4=set1^set2
print(set4) #also there are update