def solve(numheads, numlegs):
    for chikens in range(numheads):
        rabbits = numheads - chikens
        if (chikens*2 + rabbits*4) == numlegs:
            return chikens,rabbits


chikens, rabbits = solve(35,94)
print(f"There are {chikens} chikens and {rabbits} rabits")