class account():
    def __init__(s,bal,d,d1,user,w,r):
        s.w=0
        s.bal=0
        s.d=0
        s.d1=0
        s.user="unknown"
        s.r=0
    def owner(s):
        print("enter username: ")
        s.user=input()
    def balance(s):
        print("fill balance:")
        s.bal+=int(input())
        print("your balance: ",s.bal)
    def deposit(s):
        print("depositi:")
        s.r=int(input())
        if s.r<=s.bal:
            v=int(input("1 or 2:"))
            if v==1:
                s.d+=s.r
                s.bal-=s.r
            elif v==2:
                s.d1+=s.r
                s.bal-=s.r
            else:
                print("there is not 3")
        else:
            print("too much")
        print("d1: ",s.d)
        print("d2: ",s.d1)
        print("balance: ",s.bal)
    def withdraw(s):
        print("skolko?")
        s.w=int(input())
        if s.w<=s.bal:
            s.bal-=s.w
            print("poped: ",s.w)
            print("balance: ",s.bal)
        else:
            print("you are poor for it")
p=account(0,0,0,"ddd",0,0)
p.owner()
p.balance()
p.deposit()
p.balance()
p.withdraw()
p.balance()