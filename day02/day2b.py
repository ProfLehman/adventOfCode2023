# day2b.py
# j.l. lehman
# December 2, 2023
# Advent of code
#

file = open("day02/day2.txt", "r") 
#file = open("day02/day2a_test.txt", "r") 

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

    cubePower = redCount * greenCount * blueCount   
    print( f"Game {game}: red={redCount}, green={greenCount}, blue={blueCount}   cubePower={cubePower}")
    total = total + cubePower

    game = game + 1
    #end loop

print( f"Total: {total}")

file.close()
