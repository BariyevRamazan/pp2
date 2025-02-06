class shape():
    def area(self):
        return 0
    
class square(shape):
    def __init__(s,l):
        s.l=l

    def area(s):
        return s.l * s.l
a=int(input())
s=square(a)
print(s.area())
