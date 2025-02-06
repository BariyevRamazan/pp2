import movies

m=movies.movies
ca=str(input())
def ave(x):
    y=0
    l=0
    for a in x:
        if a["category"]==ca:
            y+=a["imdb"]
            l+=1
    o=y/l
    return o
avc=ave(m)
print(round(avc,2))