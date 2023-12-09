# day8a.py
# AoC Day 8: Haunted Wasteland
# 12.8.2023
#

# Read input
file = open("day08/input.txt", "r")
lines = file.readlines()

# Part 1
instruction = lines[0].strip()
print( f"|{instruction}|")

left = {}
right = {}

for i in range(2, len(lines)):
    data = lines[i].strip().split(" ")
    node = data[0]
    left_value = data[2][1:-1]
    right_value = data[3][:-1]

    #print(i, node, left, right)

    left[node] = left_value
    right[node] = right_value

print("--end read input --")

steps = 0
location = "AAA"
stop = False
while stop == False:
    for i in instruction:

        if i == "L":
            nextLocation = left[location]
        else:
            nextLocation = right[location]

        steps += 1
        location = nextLocation
        #print(steps, i, nextLocation)

        if nextLocation == "ZZZ":
            print(f"found ZZZ in {steps} steps")
            stop = True
            break   

