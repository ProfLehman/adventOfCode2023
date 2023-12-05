# day5.py
# j.l. lehman
# December 5, 2023
# Advent of code

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

"""
50 98 2
52 50 48
"""
#seedToSoil = [[50,98,2],[52,50,48]]
#test = 98
#for test in range(48,101):
#    print(test, "=>", sourceToDestination(test, seedToSoil))



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
        #print("\nnew category ...")
        continue

    elif category == "seeds":
        #print( category )
        temp = line.split()
        i = 1
        while i < len(temp):
            seeds.append( int(temp[i]) )
            i += 1
        #print( seeds )

    elif category == "seed-to-soil map:":
        #print( category )
        temp = line.split()
        #print( temp )
        seedToSoil.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( seedToSoil )

    elif category == "soil-to-fertilizer map:":
        #print( category )
        temp = line.split()
        #print( temp )
        soilToFertilizer.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( soilToFertilizer )

    elif category == "fertilizer-to-water map:":
        #print( category )
        temp = line.split()
        #print( temp )
        fertilizerToWater.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( fertilizerToWater )

    elif category == "water-to-light map:":
        #print( category )
        temp = line.split()
        #print( temp )
        waterToLight.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( waterToLight )

    elif category == "light-to-temperature map:":
        #print( category )
        temp = line.split()
        #print( temp )
        lightToTemperature.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( lightToTemperature )

    elif category == "temperature-to-humidity map:":
        #print( category )
        temp = line.split()
        #print( temp )
        temperatureToHumidity.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( temperatureToHumidity )

    elif category == "humidity-to-location map:":
        #print( category )
        temp = line.split()
        #print( temp )
        humidityToLocation.append( [int(temp[0]), int(temp[1]), int(temp[2])] )
        #print( humidityToLocation )
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


low = 100000000000000000

for seed in seeds:
    soil = sourceToDestination(seed, seedToSoil)
    fertilizer = sourceToDestination(soil, soilToFertilizer)
    water = sourceToDestination(fertilizer, fertilizerToWater)
    light = sourceToDestination(water, waterToLight)
    temperature = sourceToDestination(light, lightToTemperature)
    humidity = sourceToDestination(temperature, temperatureToHumidity)
    location = sourceToDestination(humidity, humidityToLocation)
    print( f"{seed} = > {location}") 

    if location < low:
        low = location

print( "Part A Low: ", low )




    



