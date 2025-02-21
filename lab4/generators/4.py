a=int(input())
b=int(input())
def squ():
    for i in range(a,b):
        yield i**2
ar=squ()
for i in ar:
    print(i,end=" ")