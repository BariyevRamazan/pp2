import datetime
x=datetime.datetime.now()
print("enter date in format: year month day hour minute second:")
y=input().split()
z=datetime.datetime(year=int(y[0]),month=int(y[1]),day=int(y[2]),hour=int(y[3]),minute=int(y[4]),second=int(y[5]))
print(((z-x).days)*24*60*60+(z-x).seconds)
print(z)