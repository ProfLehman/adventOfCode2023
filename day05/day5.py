# day5.py
# j.l. lehman
# December 5, 2023
# Advent of code

import sys #used for max int

# source to desired destination
def sourceToDestination(x, map):
    result = x

    for m in map:
        src = m[1]
        dst = m[0]
        rng = m[2]

        start = src
        stop = src + rng - 1
        amount = dst - src

        if x >= start and x <= stop:
            result = x + amount
            #print( f"{start} to {stop}  {x}" )
            break
           
    return result
# end sourceToDestination

# get location
def getLocation( s ):
    
    soil = sourceToDestination(s, seedToSoil)
    fertilizer = sourceToDestination(soil, soilToFertilizer)
    water = sourceToDestination(fertilizer, fertilizerToWater)
    light = sourceToDestination(water, waterToLight)
    temperature = sourceToDestination(light, lightToTemperature)
    humidity = sourceToDestination(temperature, temperatureToHumidity)
    location = sourceToDestination(humidity, humidityToLocation)
    
    return location
    # end getLocation

# build resource maps
category = "seeds"
categories = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

seeds = []

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []


filename = "day05/input.txt"
#filename = "day05/test.txt"

# read file
file = open(filename, "r") 
lines = file.readlines()

for line in lines:

    line = line.strip()

    #update category
    if line in categories:
        category = line

    elif len(line) == 0:
        continue

    elif category == "seeds":
        temp = line.split()
        i = 1
        while i < len(temp):
            seeds.append( int(temp[i]) )
            i += 1

    elif category == "seed-to-soil map:":
        temp = line.split()
        seedToSoil.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "soil-to-fertilizer map:":
        temp = line.split()
        soilToFertilizer.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "fertilizer-to-water map:":
        temp = line.split()
        fertilizerToWater.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "water-to-light map:":
        temp = line.split()
        waterToLight.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "light-to-temperature map:":
        temp = line.split()
        lightToTemperature.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "temperature-to-humidity map:":
        temp = line.split()
        temperatureToHumidity.append( [int(temp[0]), int(temp[1]), int(temp[2])] )

    elif category == "humidity-to-location map:":
        temp = line.split()
        humidityToLocation.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
    else:
        print( "Error: category", category, "not found *************************" )
    
    # end for line in lines

print( "seeds: ", len(seeds) )
print()
print( "seedToSoil: ", len(seedToSoil) )
print( "soilToFertilizer: ", len(soilToFertilizer) )
print( "fertilizerToWater: ", len(fertilizerToWater) )
print( "waterToLight: ", len(waterToLight) )
print( "lightToTemperature: ", len(lightToTemperature) )
print( "temperatureToHumidity: ", len(temperatureToHumidity) )
print( "humidityToLocation: ", len(humidityToLocation) )
print()


# ---------------------------- Part A ----------------------------
low = sys.maxsize

for seed in seeds:
    location = getLocation(seed)

    if location < low:
        low = location
        
print()
print( "Part A Low: ", low )
print()


# ---------------------------- Part B ----------------------------
low = sys.maxsize

# check seed intervals for lowest location using 25,000 increments
lowSeed = -1
i = 0
while i < len(seeds):
    startNumber = seeds[i]
    numberNeeded = seeds[i+1]
    stopNumber = startNumber + numberNeeded - 1 

    print( f"{startNumber:15d} to {stopNumber:15d} {numberNeeded:15,d}")

    j = startNumber
    while j <= stopNumber:
        
        location = getLocation(j)

        if location < low:
            low = location
            lowSeed = j
            print( f"          New Low {j:,d} = > {location:,d}")

        j += 25000
        #end while j
        
    i += 2
    # end while i

# use lowest seed to search by x1
j = lowSeed
while j >= lowSeed - 25000:
    location = getLocation(j)

    if location < low:
        low = location

    j = j - 1
    #end while j
    
print()
print( "Part B Low: ", low )
print()  

