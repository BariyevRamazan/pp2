from math import sqrt
from time import sleep
number = int(input())
time_mil = int(input())
sleep(time_mil * 10**(-3))
x = sqrt(number)
print(f"Square root of {number} after {time_mil} miliseconds is {x}")
