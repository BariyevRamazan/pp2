if 5>2:
    print("5 is greater than 2")
#-----------------------------------------------------------------------------------
#this is comment
'''
This is 
comment too
'''
#-----------------------------------------------------------------------------------
x=5
print(x)
#-----------------------------------------------------------------------------------
#If you want to specify the data type of a variable, this can be done with casting.
#   x = str(3)    # x will be '3'
#   y = int(3)    # y will be 3
#   z = float(3)  # z will be 3.0
#-----------------------------------------------------------------------------------
x = 5
y = "John"
print(type(x))
print(type(y))
#-----------------------------------------------------------------------------------
#   x = "John"   is the same as    x = 'John'
#-----------------------------------------------------------------------------------
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Money"
print(x)
print(y)
print(z)
#-----------------------------------------------------------------------------------
#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#-----------------------------------------------------------------------------------
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
print(x+y+z)
#-----------------------------------------------------------------------------------
#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
# In the print() function
# when you try to combine a string and a number with the + operator
# Python will give you an error:
#-----------------------------------------------------------------------------------
x = "3"
def myfunc():
  print("The Witcher " + x)
myfunc()

x = "ass"
def myfunc():
  x = "us"
  print("Last of " + x)

myfunc()
print("Last of " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
#-----------------------------------------------------------------------------------
#There are three numeric types in Python:
#int     5
#float   5.2
#complex 5j+2   ;   5j
#-----------------------------------------------------------------------------------
import random
print(random.randrange(1, 10))
#-----------------------------------------------------------------------------------
y = int(2.8)
print(y)
#-----------------------------------------------------------------------------------
print("Hello")
print('Hello')
#-----------------------------------------------------------------------------------
#Вы можете присвоить переменной многострочную строку, используя три кавычки:
#Или три одинарные кавычки:
a = """The Witcher 3 
is very
cool game """
print(a)
#-----------------------------------------------------------------------------------
a = "Hello, World!"
print(a[1])
#-----------------------------------------------------------------------------------
for x in "banana":
  print(x)
#-----------------------------------------------------------------------------------
#  The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
#-----------------------------------------------------------------------------------
#  Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#-----------------------------------------------------------------------------------
#  Get the characters from position 2 (included) to position 5 (not included)
b = "Hello, World!"
print(b[2:5])
#  Get the characters from the start to position 5 (not included)
b = "Hello, World!"
print(b[:5])
#  Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
#  Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])
#-----------------------------------------------------------------------------------
a = "Hello, World!"
print(a.upper())
print(a.lower())
#  The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))
#   Метод split() разбивает строку на подстроки, если находит экземпляры разделителя:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print(a.split(" ")) # returns ['Hello,', 'World!']

a = "Hello"
b = "World"
c = a + b
d = a + " " + b
print(c)
print(d)
#-----------------------------------------------------------------------------------
age = 36
txt = "My name is John, I am " + age
print(txt)

#  F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt1 = f"The price is {price:.2f} dollars"
txt2 = f"The price is {price:.3f} dollars"
print(txt1)
print(txt2)

