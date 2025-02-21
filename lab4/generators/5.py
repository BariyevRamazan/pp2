n=int(input())
def dow():
    i=n
    while i>=0:
        yield i
        i-=1
d=dow()
for i in d:
    print(i,end=" ")