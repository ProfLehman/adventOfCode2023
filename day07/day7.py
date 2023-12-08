# day7.py
# Advent of Code Day 7
# December 7th, 2023

file = open("day07/input.txt", "r") 

hands = []
bids = []

for line in file:
    str, num = line.split()
    hands.append(str)
    bids.append(int(num))

#print( hands )
#print( bids )

def countJ( h ):
    count = 0
    for i in range(0,5):
        if h[i] == 'J':
            count += 1
    return count


def handValue( h ):
    value = -1

    h = "".join(sorted(h))

    #five of a kind
    if h[0] == h[1] == h[2] == h[3] == h[4]:
        value = 7

    #four of a kind
    elif h[0] == h[1] == h[2] == h[3] or h[1] == h[2] == h[3] == h[4]:
        value = 6   
 
    #full house
    elif h[0] == h[1] == h[2] and h[3] == h[4] or h[0] == h[1] and h[2] == h[3] == h[4]:
        value = 5

    #three of a kind
    elif h[0] == h[1] == h[2] or h[1] == h[2] == h[3] or h[2] == h[3] == h[4]:
        value = 4

    #two pairs
    elif h[0] == h[1] and h[2] == h[3] or h[0] == h[1] and h[3] == h[4] or h[1] == h[2] and h[3] == h[4]:
        value = 3

    #one pair
    elif h[0] == h[1] or h[1] == h[2] or h[2] == h[3] or h[3] == h[4]:
        value = 2

    #high card
    else:
        value = 1


    #Part B - check jokers
    numJ = countJ(h)

    if numJ == 5: #four jokers - five of a kind
        value = 7
    elif numJ == 4: #four jokers - five of a kind
        value = 7
    elif numJ == 3: 
        h = h.replace("J", "")
        if h[0] == h[1]:
            value = 7 #five of a kind
        elif h[0] != h[1]:
            value = 6 #four of a kind
        else:
            print("Error with three joker values: ", h)
            value = -1

    elif numJ == 2: #two jokers
        h = h.replace("J", "")
        
        if h[0] == h[1] == h[2]: # five of a kind
            value = 7
        elif h[0] == h[1] or h[1] == h[2] or [0]== h[2]: # four of a kind
            value = 6
        elif h[0] != h[1] and h[1] != h[2]:
            value = 4 # three of a kind
        else:
            print("Error with two joker values: ", h)
            value = -1

    elif numJ == 1:
        h = h.replace("J", "")
        
        if h[0] == h[1] == h[2] == h[3]: #five of a kind
            value = 7 
        elif h[0] == h[1] == h[2] or h[0] == h[1] == h[3]: #four of a kind 
            value = 6
        elif h[0] == h[2] == h[3] or h[1] == h[2] == h[3]: #four of a kind 
            value = 6
        elif h[0] == h[1] and h[2] == h[3] or h[0] == h[2] and h[1] == h[3] or h[0] == h[3] and h[1] == h[2]:
            value = 5 #full house
        elif h[0] == h[1] or h[1] == h[2] or h[2] == h[3] or h[0] == h[2] or h[1] == h[3] or h[0] == h[3]:
            value = 4 #three of a kind
        elif h[0] != h[1] and h[1] != h[2] and h[2] != h[3]:
            value = 2
        else:
            print("Error with one joker value: ", h)
            value = -1
    elif numJ == 0:
        value = value
    else:
        print("Error with jokers: ", h)

    return value


def compareHands( h1, h2 ):

    #Part A
    #values = "23456789TJQKA"

    #Part B
    values = "J23456789TQKA"

    if handValue(h1) < handValue(h2):
        return True
    elif handValue(h1) > handValue(h2):
        return False
    else:
        #same hand value, compare cards
        for i in range(0,5):
            if values.find(h1[i]) < values.find(h2[i]):
                return True
            elif values.find(h1[i]) > values.find(h2[i]):
                return False
        print("Error in compareHands")
 

# sort hands and bids using insertion sort low to high
p = 1
while p < len(hands):
    
    i = p
    while i > 0 and compareHands(hands[i], hands[i-1]):
        hands[i], hands[i-1] = hands[i-1], hands[i]
        bids[i], bids[i-1] = bids[i-1], bids[i]
        i -= 1

    p = i + 1

#print( hands )
#print( bids  )
print()

# add up winnings
winnings = 0
m = 1
for b in bids:
    winnings = winnings + (b*m)
    m = m + 1


print( "Winnings: ", winnings )


