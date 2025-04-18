import math
n=int(input())
def squ():
        yield i**2
a=squ()
next(a)
next(a)
print(next(a))