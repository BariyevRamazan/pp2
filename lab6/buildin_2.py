x = str(input())
y = x.lower()
upper_case = 0
lower_case = 0
for i in range(len(x)):
    if(x[i] == y[i]):
        lower_case += 1
    else:
        upper_case += 1
print(f"There is {upper_case} upper case and {lower_case} lower case")
