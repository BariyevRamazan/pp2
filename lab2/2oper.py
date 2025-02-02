x=7
k=0
while(x!=1):
    k+=1
    x%=3
print(k)
y=9
y//=2
p=4
p**=3
print(y, p)
print(x:=3)
c=int(input())
if c>0 and c<88:
    print("and")
elif c<0 or c>88:
    print("or")
else:
    print(14)
y=["2ch",'4ch']
x="dvach"
print(x in y)
x=545545454
print(~x)