import math
n=int(input())
def squ():
    for i in range(n):
        yield i**2
a=squ()
next(a)
next(a)
print(next(a))