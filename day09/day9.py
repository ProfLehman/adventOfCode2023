# day9.py
# AoC Day 9: Mirage Maintenance
# 9 December 2023

# process sequence
def processSequence( s2, day ):

    s = s2.copy() # note: lists are passed by reference, so copy it

    stop = False
    N = len( s )
    Last = N
    startN = N
    i = 1

    while not stop:
        # process line
        s.append(0)
        difCount = 0
        while i < Last:
            dif = s[i] - s[i-1]
            s.append( dif )
            if dif == 0:
                difCount += 1
            i = i + 1
        Last = Last + N
        N = N - 1
        i = i + 2 #skip over last and start at next "1"
        if difCount == N:  #stop when all zeros
            stop = True
            s.append(0)
            #print( s )

            N = N + 1
            Last = Last - N
            
            #print( N, Last)
            v = 0
            while N <= startN:
                
                if day == 1:
                    #Part A.
                    s[Last] = s[Last-1] + s[Last+N]
                    #print( "debug", Last, Last-1, Last+N )
                else:
                    #Part B.
                    s[Last] = s[Last-N] - s[Last+N]
                    #print( "debug", Last, Last-N, Last+N )
                
                N += 1
                Last = Last - N
                #print( N, Last)
        # while not stop

    return s[startN]
    # end function processSequence

# read data
lines = open('day09/input.txt').read().splitlines()
#print( lines )

# Part 1 & Part 2
print()
# debug
#print( processSequence( [0, 3, 6, 9, 12, 15] ) )
#print( processSequence( [1, 3, 6, 10, 15, 21] ) )

total1 = 0
total2 = 0

for line in lines:
    line = [int(i) for i in line.split()]
    #print(line)

    v = processSequence(line, 1)
    #print( v )
    total1 = total1 + v

    v = processSequence(line, 2)
    #print( v )
    total2 = total2 + v

print( "Part A:", total1 )
print( "Part B:", total2 )


