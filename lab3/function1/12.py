def schw(list):
    for x in list :
        for y in range(x+1) :
            print("*", end = "")
        print("")

list = list(map(int,input().split()))
schw(list)