# day1a.py
# j.l. lehman
# December 1, 2023
# Advent of code
#
# read list of strings
# find the first and last digits in the string to form a two digit number
# add all numbers from each line and output sum
#

# find and return first digit in string
def firstDigit( s ):
    for digit in s:
        if digit.isdigit():
            return digit
    return -1    

# find and return first digit in string
def lastDigit( s ):
    return firstDigit( reversed(s) )    


file = open("day01/data/day1a.txt", "r") 

lines = file.readlines()
#print( lines )

total = 0

for line in lines:
    line = line.strip()
    first = firstDigit(line)
    last = lastDigit(line)

    number = int( first+last )
    total += number
    print( f"{line} {first} {last} {number}" )

print( total )







