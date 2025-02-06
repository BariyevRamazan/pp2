def schw(t) :
    if(len(t) < 3 ) :
        return False
    for x in range( 1, len(t) - 1 ) :
        if t[x] == 0 and t[x-1] == 0 and t[x+1] == 7 : 
            return True
    return False

t = list(map(int, input().split()))
result = schw(t)
print(result)