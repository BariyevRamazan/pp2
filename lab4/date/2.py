import datetime
x=datetime.datetime.now()
for y in range(-1,2):
    print((x+datetime.timedelta(days=y)).strftime("%x"))
