import agrade1

m=agrade1.mov
def pri(x):
    if agrade1.grade(x["imdb"]):
        print(x)
for x in m:
    pri(x)