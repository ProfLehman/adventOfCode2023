# da4.py
# j.l. lehman
# December 4, 2023
# Advent of code
# 

# read and process each line 
#filename = "day04/test.txt"  
filename = "day04/parta.txt"

file = open(filename, "r") 
lines = file.readlines()

parta = 0

matches = [] #number of matches for card by card number
cards = []  #number of cards by card number

matches.append(0) #dummy
cards.append(0) #dummy

card = 1
for line in lines:
    
    line = line.strip() #remove trailing /n
    data = line.split()
    mid = data.index("|")

    #print( data )
    winners = data[1:mid]
    mine = data[mid+1:]
    #print( "w:", winners )
    #print( "m:", mine )
    #print()

    count = 0
    for m in mine:
        if m in winners:
            count = count + 1

    if count > 0:        
        parta = parta + pow(2,count-1) 

    print( f"card {card}: count: {count}" )
    matches.append(count)
    cards.append(1)

    card = card + 1
    #end loop

# output parta
print()
print( "parta: ", parta )
print( matches)
print( cards )


i = 1
while i < len(cards):

    num = matches[i]

    j = 1
    while j <= num:
        cards[i+j] = cards[i+j] + cards[i]

        j = j + 1
        #while

    i = i + 1 
    #while

print(cards[1:])
print( "part b: ", sum(cards) )