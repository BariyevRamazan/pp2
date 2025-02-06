import math
class point():
    def __init__(self,i,j):
        self.i=i
        self.j=j
        #self.n=n
        #self.m=m
    def show(s):
        print(s.i,s.j)
    def move(s):
        s.i=int(input())
        s.j=int(input())
    def dist(s):
        s.n=int(input())
        s.m=int(input())
        return math.sqrt(((s.n-s.i)**2)+((s.m)-s.j)**2)
u=point(7,8)
u.show()
u.move()
u.show()
print(round(u.dist(),2))
