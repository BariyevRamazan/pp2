from itertools import permutations

def schw(s):
    result = [''.join(p) for p in permutations(s)]
    return result

word = input()
result = schw(word)
print(result)