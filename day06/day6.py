# day6.py
# j.l. lehman
# December 7, 2023
# Advent of code

file = open("day06/input2.txt", "r") 

#split and convert all items after 1 to int list
time = [int(i) for i in file.readline().split()[1:]]
distance = [int(i) for i in file.readline().split()[1:]]

print( time )
print( distance )

partA = 1

race = 0
while race < len(time):
    
    # multiple trials for each race
    winCount = 0
    t = time[race]
    d = distance[race]

    for h in range(1,t+1):
        trial = (t - h) * h
        #print( trial )
        if trial > d:
            winCount = winCount + 1
    
    print( winCount )
    partA = partA * winCount
    print()

    race = race + 1
    # end while race

print( "partA: ", partA )   




