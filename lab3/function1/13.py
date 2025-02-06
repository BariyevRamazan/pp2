import random
a=random.randint(1,20)
print( "Hello! What is your name?" )
print("KBTU")
print("")
print("Well, KBTU, I am thinking of a number between 1 and 20")
print("")
b = False
n = 0
while b == False :
    print("Take a guess.")
    digit = int(input())
    if digit == a :
        b = True
    elif digit<a :
        print("")
        print("Your guess is too low.")
    else :
        print("")
        print("Your guess is too high.")
    n+=1
print("")
print(f"Good job, KBTU! You guessed my number in {n} guesses!")