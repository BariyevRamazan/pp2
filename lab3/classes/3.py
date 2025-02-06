class shape():
    def area(s):
        return 0
    
class rect(shape):
    def __init__(s,l,b):
        s.l=l
        s.b=b

    def area(s):
        return s.l * s.b
a=int(input())
b=int(input())
s=rect(a,b)
print(s.area())
