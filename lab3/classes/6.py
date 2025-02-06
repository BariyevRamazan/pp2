def checker(x):
    i=2
    b=True
    while i<x:
        if x%i==0:
            b=False
            break
        i+=1
    return b 

class prime():
    def __init__(self,o):
        self.o=o
    def filter(s):
        i=0
        while i<len(s.o):
            if checker(s.o[i]) and s.o[i]!=1:
                print(s.o[i])
            i+=1
lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
p=prime(lis)
p.filter()