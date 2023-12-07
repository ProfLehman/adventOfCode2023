file = open("day07/test.txt", "r") 

hands = []
bids = []

for line in file:
    str, num = line.split()
    hands.append(str)
    bids.append(int(num))

print( hands )
print( bids )


# Part A
#def equal( a, b):
#    return a == b

# Part B
def eq( a, b):
    if a == b or a == "J" or b == "J":
        return True
    else:
        return False

def handValue( h ):
    value = -1

    h = sorted(h)

    #five of a kind
    #if h[0] == h[1] == h[2] == h[3] == h[4]:
    if eq(h[0], h[1]) and eq(h[1], h[2]) and eq(h[2], h[3]) and eq(h[3], h[4]):
        value = 7

    #four of a kind
    #elif h[0] == h[1] == h[2] == h[3] or h[1] == h[2] == h[3] == h[4]:
    elif eq(h[0], h[1]) and eq(h[1], h[2]) and eq(h[2], h[3]) or eq(h[1], h[2]) and eq(h[2], h[3]) and eq(h[3], h[4]):
        value = 6   

    #full house
    #elif h[0] == h[1] == h[2] and h[3] == h[4] or h[0] == h[1] and h[2] == h[3] == h[4]:
    elif eq(h[0], h[1]) and eq(h[1], h[2]) and eq(h[3], h[4]) or eq(h[0], h[1]) and eq(h[2], h[3]) and eq(h[3], h[4]):
        value = 5

    #three of a kind
    #elif h[0] == h[1] == h[2] or h[1] == h[2] == h[3] or h[2] == h[3] == h[4]:
    elif eq(h[0], h[1]) and eq(h[1], h[2]) or eq(h[1], h[2]) and eq(h[2], h[3]) or eq(h[2], h[3]) and eq(h[3], h[4]):
        value = 4

    #two pairs
    #elif h[0] == h[1] and h[2] == h[3] or h[0] == h[1] and h[3] == h[4] or h[1] == h[2] and h[3] == h[4]:
    elif eq(h[0], h[1]) and eq(h[2], h[3]) or eq(h[0], h[1]) and eq(h[3], h[4]) or eq(h[1], h[2]) and eq(h[3], h[4]):
        value = 3

    #one pair
    #elif h[0] == h[1] or h[1] == h[2] or h[2] == h[3] or h[3] == h[4]:
    elif eq(h[0], h[1]) or eq(h[1], h[2]) or eq(h[2], h[3]) or eq(h[3], h[4]):
        value = 2

    #high card
    else:
        value = 1

    return value

def compareHands( h1, h2 ):

    #Part A
    values = "23456789TJQKA"

    #Part B
    #values = "J23456789TQKA"

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

print( hands )
print( bids  )
print()

# add up winnings
winnings = 0
m = 1
for b in bids:
 winnings = winnings + (b*m)
 m = m + 1


print( "Part A. winnings: ", winnings )


print()
for hand in hands:
    print( hand, handValue(hand) )
    print() 


