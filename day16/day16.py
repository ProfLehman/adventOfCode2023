# day16.p7
# 12/16/2020
# Advent of Code 2023
# Day 16: The Floor Will Be Lava 

# Part 1

# load the grid
fn = "day16/test.txt"
#fn = "day16/input.txt"

file = open(fn, "r")
lines = file.readlines()

grid = {}

for row, line in enumerate(lines):
    for col, char in enumerate(line.strip()):
        grid[f"{row},{col}"] = char

# Get the maximum row and column indices
max_row = max(int(key.split(',')[0]) for key in grid)
max_col = max(int(key.split(',')[1]) for key in grid)

print("Number of items in grid:", len(grid))
print("max row and col (acutal last index)", max_row, max_col)

"""
# Print the grid
for row in range(max_row + 1):
    for col in range(max_col + 1):
        print(grid.get(f"{row},{col}", ' '), end="")
    print()
print()
"""

def onGrid(row, col):
    return row >= 0 and row <= max_row and col >= 0 and col <= max_col

# Part 1
def shineBeams( start ):
    energized = {}
    path = {}

    # start with the first beam
    beams = [ start ]

    while len(beams) > 0:
        #print( "Number of beams:", len(beams) )

        # get the next beam
        beam = beams.pop(0)
        row, col, direction = beam
        #print("Beam:", row, col, direction)

        # check if beam is off the grid
        if onGrid(row, col):
           
            # set energized (may set multiple times)
            energized[f"{row},{col}"] = True
            
            # add to path if not already there
            path_key = f"{row},{col},{direction}"
            if path_key not in path:
                path[path_key] = True

                # move beam
                tile = grid.get(f"{row},{col}", 'E')
                #print("Tile:", tile)

                if tile == ".":
                    # keep going
                    if direction == "N":
                        beams.append( [row-1, col, "N"] )
                    elif direction == "S":
                        beams.append( [row+1, col, "S"] )
                    elif direction == "E":              
                        beams.append( [row, col+1, "E"] )
                    elif direction == "W":            
                        beams.append( [row, col-1, "W"] )
                    else:              
                        print("********** Invalid direction at .:", direction)


                if tile == "|":
                    # keep going
                    if direction == "N":
                        beams.append( [row-1, col, "N"] )
                    elif direction == "S":
                        beams.append( [row+1, col, "S"] )
                    elif direction == "E" or direction == "W":              
                        beams.append( [row+1, col, "S"] )
                        beams.append( [row-1, col, "N"] )
                    else:              
                        print("********** Invalid direction at |:", direction)

                if tile == "-":
                    # keep going
                    if direction == "E":
                        beams.append( [row, col+1, "E"] )
                    elif direction == "W":
                        beams.append( [row, col-1, "W"] )
                    elif direction == "N" or direction == "S":              
                        beams.append( [row, col+1, "E"] )
                        beams.append( [row, col-1, "W"] )
                    else:              
                        print("********** Invalid direction at -:", direction)

                if tile == "/":
                    # keep going
                    if direction == "E":
                        beams.append( [row-1, col, "N"] )
                    elif direction == "W":
                        beams.append( [row+1, col, "S"] )
                    elif direction == "N":              
                        beams.append( [row, col+1, "E"] )
                    elif direction == "S":
                        beams.append( [row, col-1, "W"] )
                    else:              
                        print("********** Invalid direction at -:", direction)

                if tile == "\\":
                    # keep going
                    if direction == "E":
                        beams.append( [row+1, col, "S"] )
                    elif direction == "W":
                        beams.append( [row-1, col, "N"] )
                    elif direction == "N":              
                        beams.append( [row, col-1, "W"] )
                    elif direction == "S":
                        beams.append( [row, col+1, "E"] )
                    else:              
                        print("********** Invalid direction at \\:", direction)

            #if key not in path
                        
        # if onGrid(row, col)

    # end while len(beams) > 0

    # Print the energized
                        """
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            if f"{row},{col}" in energized:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    """
                        
    return len(energized)
    # end function shineBeams()


# *********************** Main **********************

print( "Part 1.", shineBeams([0,0,"E"]) )

max = -1
for c in range(max_col + 1):
    value = shineBeams([0,c,"S"])
    if value > max:
        max = value

    value = shineBeams([max_row,c,"N"])
    if value > max:
        max = value

print( "done top bottom", max )

for r in range(max_row + 1):
    value = shineBeams([r,0,"E"])
    if value > max:
        max = value

    value = shineBeams([r,max_col,"W"])
    if value > max:
        max = value

print( "Part 2.", max )
