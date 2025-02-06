import movies
m=movies.movies

def ave(x):
    y=0
    for a in x:
        y+=a["imdb"]
    o=y/len(x)
    return o
av=ave(m)
print(round(av,2))