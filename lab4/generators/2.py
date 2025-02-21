n=int(input())
def ev():
    for i in range(n):
        if i%2==0:
            yield i
a=ev()
for i in a:
    if n%2==0:
        o=n-2
    else:
        o=n-1
    print(i,end='')
    if i<o:
        print(',',end='')
    