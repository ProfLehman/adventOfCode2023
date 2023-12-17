# day11.p7
# 12/16/2023
# Advent of Code 2023
# Day 11:  

# Part 1

# load the grid
fn = "day11/test.txt"
fn = "day11/input.txt"

file_in = open(fn, "r")

lines = file_in.readlines()

blank_row_count = 0
blank_col_count = 0

#expand columns
i = 0
while i < len(lines[0]):

    #see if all blank at column i
    all_blank = True
    for line in lines:
        if line[i] != ".":
            all_blank = False
            break
    
    if all_blank:
        blank_col_count = blank_col_count + 1
        #insert column
        for j in range(len(lines)):
            temp_copy = lines[j]
            temp_copy = temp_copy[:i] + "." + temp_copy[i:]
            lines[j] = temp_copy
        i = i + 1   
    
    i = i + 1

# expand lines
i = 0
while i < len(lines):
    if lines[i].find("#") == -1:
        blank_row_count = blank_row_count + 1
        temp_copy = lines[i]        
        lines.insert(i, temp_copy)
        i = i + 2
    else:
        i = i + 1

print(f"Blank row count: {blank_row_count}")
print(f"Blank col count: {blank_col_count}")


#for line in lines:
#    print( line )

file_in.close()

# find galaxies

nodes = []

row = 0
for line in lines:
    for col in range(len(line)):
        if line[col] == "#":
            nodes.append( [row,col] )
    row = row + 1

#print( nodes )
print()

from itertools import combinations

part1_sum = 0

for combination in combinations(nodes, 2):
    #print(combination)

    node1, node2 = combination
    x1, y1 = node1
    x2, y2 = node2
    #print(f"Node 1: ({x1}, {y1}), Node 2: ({x2}, {y2})")
    hamming_distance = abs(x1 - x2) + abs(y1 - y2)
    #print(f"Hamming distance: {hamming_distance}")
    part1_sum = part1_sum + hamming_distance

print(f"Part 1 sum: {part1_sum}")