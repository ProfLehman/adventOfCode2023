# day3a.py
# j.l. lehman
# December 3, 2023
# Advent of code
#

class Schematic:
    def __init__(self):
        self.map = {} #dictionary of all data in schematic
        self.ok = {} #dictionary of OK locations
        self.numbers = [] #list of numbers schematic
      
    def readSchematic(self, filename):

        # reset schematic
        self.map = {} #dictionary of all data in schematic
        self.ok = {} #dictionary of OK locations
        self.numbers = [] #list of numbers schematic

        # read and process each line    
        file = open(filename, "r") 
        lines = file.readlines()

        row = 0
        for line in lines:
            #process line
            line = line.strip() #remove trailing /n

            col = 0
            while col < len(line):
                
                if line[col] != ".":
                    key = f"{row},{col}"
                    self.map[ key ] = line[col]

                # update OK map with all surrounding locations

                # add to current number

                # add number to list of numbers



                col = col + 1
            #end process line

            row = row + 1
        #end for each line

        file.close()

    def solve(self, filename):
        self.readSchematic(filename)
        print(f"Part A: {-1}")

    def debug(self):
        print("*** DEBUG ***")
        #for key, value in self.map.items():
        #    print(f"{key} = {value}")

# ---- main ----
partA = Schematic()
partA.solve("day03/test_a.txt")
#partA.solve("day03/a.txt")

partA.debug()


