def schw(t) :
    for x in range( 1, len(t)) :
        if t[x] == 3 and t[x-1] == 3: 
            return True
    return False

t = list(map(int, input().split()))
result = schw(t)
print(result)



        