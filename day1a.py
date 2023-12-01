# day1a.py
# j.l. lehman
# December 1, 2023
# Advent of code
#
# read list of strings
# find the first and last digits in the string to form a two digit number
# add all numbers from each line and output sum
#

file = open("data/day1a.txt", "r") 

lines = file.readlines()
print( lines )

for line in lines:
    print( line.strip() )





