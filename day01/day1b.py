# day1b.py
# j.l. lehman
# December 1, 2023
# Advent of code
#
# read list of strings
# find the first and last digits in the string to form a two digit number
# add all numbers from each line and output sum
# in this variation the numbers may be words also ie. one, two, nine, sixteen


# find and return first digit in string
def firstDigit( s ):
    for digit in s:
        if digit.isdigit():
            return digit
    return -1    

# find and return first digit in string
def lastDigit( s ):
    return firstDigit( reversed(s) )    

# remove first words
def removeWords(s):

    # must account for overlapping digit names
    s = s.replace("oneight", "oneeight")
    s = s.replace("twone", "twoone")
    s = s.replace("threeight", "threeeight")
    s = s.replace("fiveight", "fiveeight")
    s = s.replace("sevenine", "sevennine")
    s = s.replace("eightwo", "eighttwo")
    s = s.replace("eighthree", "eightthree")
    s = s.replace("nineight", "nineeight")

    words = ["-----", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    stop = False

    while stop == False:

        #first first occurance of word
        firstPos = len(s)
        firstIndex = -1
        firstWord = "unknown"
        i = 0
        while i < len(words):
            pos = s.find(words[i])
            if pos != -1 and pos < firstPos:
                firstPos = pos
                firstIndex = i
                firstWord = words[i]

            i = i + 1
            #while

        #print( firstIndex, firstWord )

        # replace occurance of word
        if firstIndex != -1:
            s = s.replace(firstWord, str(firstIndex) )
        else:
            stop = True
    
    return s


# open file 
file = open("day01/data/day1a.txt", "r") 
lines = file.readlines()
#print( lines )

total = 0

for line in lines:
    line = line.strip()
    print(line)
    line = removeWords(line)

    first = firstDigit(line)
    last = lastDigit(line)

    number = int( first+last )
    total += number
    print( f"{line} {first} {last} {number}" )
    print()
  
print( total )

