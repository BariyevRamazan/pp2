def schw(x):
    words = x.split()
    w = words[::-1]
    e = ' '.join(w)
    return e

x = input()
print(schw(x))
