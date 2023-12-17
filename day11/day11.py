# day11.p7
# 12/16/2023
# Advent of Code 2023
# Day 11:  

# Part 1 & 2 - math approach

# load the grid
fn = "day11/test.txt"
fn = "day11/input.txt"

distance = 1000000

file_in = open(fn, "r")
lines = file_in.readlines()
for line in lines:
    line = line.strip()
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


blank_rows = []
blank_cols = []

#expand columns
for col in range(len(lines[0])):
    #see if all blank at column i
    all_blank = True
    for line in lines:
        if line[col] != ".":
            all_blank = False
            break  
    if all_blank:
        blank_cols.append(col)

# expand rows
for row in range(len(lines)):
    if lines[row].find("#") == -1:
        blank_rows.append(row)

print("blank rows:", blank_rows)
print("blank cols:", blank_cols)

import copy

new_nodes = copy.deepcopy(nodes)

for br in blank_rows:
    i = 0
    while i < len(nodes):
        if nodes[i][0] > br:
            new_nodes[i][0] = new_nodes[i][0] + (distance - 1)
        i = i + 1

for cr in blank_cols:
    i = 0
    while i < len(nodes):
        if nodes[i][1] > cr:
            new_nodes[i][1] = new_nodes[i][1] + (distance - 1)
        i = i + 1

nodes = new_nodes

#for line in lines:
#    print( line )

#print( nodes )

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