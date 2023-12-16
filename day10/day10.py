# day10.py
# Day 10: Pipe Maze 
# 15 December 2023

import sys

sys.setrecursionlimit(50000)

# help with finding inside I
# https://www.quora.com/How-do-I-know-a-point-is-inside-a-closed-curve-or-not
#
# switched to flood fill algorithm
# used hints for zooming in to allow floodfill to work


filename = "day10/input.txt"
grid = {}
grid2 = {}
path = {}
start_key = None

inside_count = 0

max_row = -1
max_col = -1

with open(filename, 'r') as file:
    for row, line in enumerate(file):
        if row > max_row:
            max_row = row
        for col, value in enumerate(line.strip()):
            if col > max_col:
                max_col = col
            grid[(row,col)] = value
            if value == 'S':
                start_key = (row, col)

#for key, value in grid.items():
#    print(key, value)
print( max_row, max_col)

print(f"The start key is: {start_key}")




def traverse(current_key, current_direction, current_steps):
  
    d  = ["N", "S", "E", "W", "N", "N", "S", "S", "E", "E", "W", "W", "N", "S", "E", "W"]
    t  = ["|", "|", "-", "-", "7", "F", "J", "L", "J", "7", "L", "F", "S", "S", "S", "S"]
    r  = [ -1,   1,   0,   0,   0,  0,   0,   0,  -1,   1,  -1,    1,  -1,   1,   0,   0]
    c  = [  0,   0,   1,  -1,  -1,   1,  -1,   1,  0,   0,   0,    0,   0,   0,   1,  -1]
    nd = ["N", "S", "E", "W", "W", "E", "W", "E", "N", "S", "N", "S", "N", "S", "E", "W"]

    while True:
    
        current_x, current_y = current_key  

        if current_key == start_key and current_steps > 0:
            #print(f"Starting at {current_key} facing {current_direction}")
            print( "Path Completed")
            return current_steps
        else:
            current_tile = grid[current_key]

            stop = False
            for i in range(16):
                if current_direction == d[i] and current_tile == t[i]:
                    current_key = (current_x + r[i], current_y + c[i])
                    current_direction = nd[i]
                    current_steps = current_steps + 1
                    path[(current_x, current_y)] = current_tile #v[i]  #was pt[i]
                    stop = False

            if stop:
                print("Error: no path found", current_steps)
                return -1


def floodFill( current_row, current_col, fill_value):
    
    if current_row >= 0 and current_row <= max_row and current_col >= 0 and current_col <= max_col: 
        key = (current_row, current_col)

        if grid2[key] == ".":
            grid2[key] = fill_value

            floodFill( current_row-1, current_col-1, fill_value)
            floodFill( current_row-1, current_col, fill_value)
            floodFill( current_row-1, current_col+1, fill_value)
            floodFill( current_row, current_col-1, fill_value)
            floodFill( current_row, current_col+1, fill_value)
            floodFill( current_row+1, current_col-1, fill_value)
            floodFill( current_row+1, current_col, fill_value)
            floodFill( current_row+1, current_col+1, fill_value)

def zoomIn():

    global max_row
    global max_col

    t =    [ "|",    "-",   "7",   "F",   "J",   "L",   "S",  "."]
    a =    [".|.",  "...", "...", "...", ".|.", ".|.", "...", "..."]
    b =    [".|.",  "---", "-7.", ".F-", "-J.", ".L-", ".S-", ".B."]
    c =    [".|.",  "...", ".|.", ".|.", "...", "...", ".|.", "..."]
  
    file2 = open("day10/temp.txt", 'w')

    for row in range(0, max_row + 1):
        line1 = ""
        line2 = ""
        line3 = ""
        for col in range(0, max_col + 1):
            key = (row,col)
            temp = grid[key]
            if key in path:
                pos = t.index(temp)
                line1 = line1 + a[pos]
                line2 = line2 + b[pos]
                line3 = line3 + c[pos]
            else:
                line1 = line1 + "..."
                line2 = line2 + ".B."
                line3 = line3 + "..."
        print(line1)
        print(line2)
        print(line3)
        file2.write(line1 + "\n")
        file2.write(line2 + "\n")
        file2.write(line3 + "\n")

    file2.close()
    
    file3 = open("day10/temp.txt", 'r')

    lines = file3.readlines()
    max_col = len( lines[0] )-2
    row = 0

    for line in lines:
 
        col = 0
        while col < len(line)-1:
            grid2[(row,col)] = line[col]
            col = col + 1
        row = row + 1

    max_row = row - 1

    print( max_row, max_col)
    file3.close()   


# --- main ---

start_direction = "S"
total_steps = traverse(start_key, start_direction, 0) 

print(f"Total steps: {total_steps}")
half_steps = total_steps // 2
print(f"Half steps: {half_steps}")


# dislay the grid
for row in range(max_row + 1):
    for col in range(max_col + 1):
        key = (row,col)
        if key in path or grid[key] == ".":
            print( grid[key], end="")
        else:
            grid2[key] = "."
            print( ".", end="")
        
    print()
print()


zoomIn()


print()

floodFill(50, 77, "I")

#print( grid2 )
inside_count2 = 0

print( max_row, max_col)

file4 = open("day10/output.txt", 'w')

for row in range(max_row):
    for col in range(max_col):
        key = (row,col)
        print( grid2[key], end="")
        file4.write( grid2[key] )
        if col >= 1 and col <= max_col - 1 and row >= 1 and row <= max_row - 1:
            if grid2[key] == "B":
                if  grid2[(row-1,col-1)] == "I" and grid2[(row-1,col)] == "I" and grid2[(row-1,col+1)] == "I" and grid2[(row,col-1)] == "I" and grid2[(row,col+1)] == "I" and grid2[(row+1,col-1)] == "I" and grid2[(row+1,col)] == "I" and grid2[(row+1,col+1)] == "I":
                    inside_count2 = inside_count2 + 1
    print()
    file4.write("\n")
    
file4.close()

print( "Inside count: ", inside_count2)

