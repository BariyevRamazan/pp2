def schw(word) :
    x = int(len(word)/2)
    if word[0] != word[len(word) - 1] :
        return False
    for y in range( 1 , x+1 ):
        if word[y] != word[-y - 1] :
            return False
    return True

word = str(input())
result = schw(word)
print(result)

