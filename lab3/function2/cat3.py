import  movies
m=movies.movies
cat=str(input())
def c(x):
    if(x["category"]==cat):
        return x["name"]
f=[]
for x in m:
    if c(x)!=None:
        f.append(c(x))
print(f)
