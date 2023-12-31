# day2a.py
# j.l. lehman
# December 2, 2023
# Advent of code
#
# AI generated description

# Determines the maximum number of each color in each game
# and adds the game number to the total if the maximums are
# less than the maximums allowed.
#
# The input file is a list of games. Each game is a list of pulls.
# Each pull is a color and a number. The color is red, green, or blue.
# The number is between 1 and 20 inclusive.
# The maximum number of each color is redMax, greenMax, and blueMax.
# The maximums are 12, 13, and 14 respectively.
# The total is the sum of the game numbers.


#file = open("day02/day2.txt", "r") 
file = open("day02/day2a_test.txt", "r") 

lines = file.readlines()

redMax = 12
greenMax = 13
blueMax = 14


total = 0

game = 1
for line in lines:
    line = line.strip()
    #print( line )

    # remove game header
    line = line[line.find(":")+2:]
    #print( line)

    redCount = 0
    blueCount = 0
    greenCount = 0
    
    games = line.split(";")
    for g in games:
        g = g.strip() # remove leading and trailing spaces

        for pull in g.split(","):
            pull = pull.strip()
            #print( pull )
            data = pull.split(" ")
            num = int(data[0])
            color = data[1]
            #print( num, color )

            if color == "red":
                if num > redCount:
                    redCount = num
            elif color == "blue":
                if num > blueCount:
                    blueCount = num
            elif color == "green": 
                if num > greenCount:
                    greenCount = num
            else:
                print( "ERROR: unknown color", color)
            #end if
            
            #end loop

    if redCount <= redMax and blueCount <= blueMax and greenCount <= greenMax:
        print( f"Game {game}: red={redCount}, green={greenCount}, blue={blueCount} ")
        total = total + game

    game = game + 1
    #end loop

print( f"Total: {total}")

file.close()
