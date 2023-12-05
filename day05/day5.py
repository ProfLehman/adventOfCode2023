# day5.py
# j.l. lehman
# December 5, 2023
# Advent of code

# source to desired destination
def sourceToDestination(x, map):
    result = x

    for m in map:
        src = m[1]
        dst = m[0]
        rng = m[2]

        start = src
        stop = src + rng - 1
        amount = dst - src

        if x >= start and x <= stop:
            result = x + amount
            #print( f"{start} to {stop}  {x}" )
            break
           
    return result
# end sourceToDestination

"""
50 98 2
52 50 48
"""

seedToSoil = [[50,98,2],[52,50,48]]

#test = 98
for test in range(48,101):
    print(test, "=>", sourceToDestination(test, seedToSoil))



