# day3.py
# j.l. lehman
# December 3, 2023
# Advent of code
#

from typing import Any


class Schematic:
    def __init__(self):
        self.map = {} #dictionary of all data in schematic
        self.ok = {} #dictionary of OK locations
        self.numRows = 0
        self.numCols = 0

    def solveA(self, filename):
        self.readSchematic(filename)
        print(f"Part A: {self.checkNumbers()}\n\n")

    def solveB(self, filename):
        self.readSchematic(filename)
        print(f"Part B: {self.findCogs()}\n\n")

    def debug(self):
        print("\n*** map ***")
        for key, value in self.map.items():
            print(f"{key} = {value}")

        print("\n*** ok map ***")
        for key, value in self.ok.items():
            print(f"{key} = {value}")


    def readSchematic(self, filename):

        # reset schematic
        self.map = {} #dictionary of all data in schematic
        self.ok = {} #dictionary of OK locations

        # read and process each line    
        file = open(filename, "r") 
        lines = file.readlines()

        self.numCols = len(lines[0].strip())

        row = 0
        for line in lines:
            #process line
            line = line.strip() #remove trailing /n

            col = 0
            while col < len(line):
                
                #if not blank
                if line[col] != ".":

                    #add digit or symbol to map
                    key = f"{row},{col}"
                    self.map[ key ] = line[col]

                    #update OK map around non-digit symbol
                    if not line[col].isdigit():
                        self.ok[ f"{row},{col-1}" ] = True
                        self.ok[ f"{row},{col+1}" ] = True
                        self.ok[ f"{row-1},{col-1}" ] = True
                        self.ok[ f"{row-1},{col}" ] = True
                        self.ok[ f"{row-1},{col+1}" ] = True
                        self.ok[ f"{row+1},{col-1}" ] = True
                        self.ok[ f"{row+1},{col}" ] = True
                        self.ok[ f"{row+1},{col+1}" ] = True

                col = col + 1
            #end process line

            row = row + 1
        #end for each line

        self.numRows = row

        file.close()

        print(f"numRows = {self.numRows}")
        print(f"numCols = {self.numCols}")
        print()


    def checkNumbers(self):
        total = 0

        for row in range(-1, self.numRows+1):
            
            number = ""
            foundNumber = False
            validNumber = False
            shouldCheck = False

            for col in range(-1, self.numCols+1):

                key = f"{row},{col}"

                # add number to number
                if key in self.map:
                    if self.map[key].isdigit():
                        
                        foundNumber = True

                        if key in self.ok:
                            validNumber = True

                        number = number + self.map[key]
                    else:
                        shouldCheck = True
                else:
                    shouldCheck = True

                # if space or symbol check number
                if shouldCheck == True:
                    if foundNumber == True and validNumber == True:
                            #print( "Adding ", number )
                            total = total + int(number)

                    number = ""
                    foundNumber = False
                    validNumber = False
                    shouldCheck = False

        return int(number)

    def findMiddle(self, row, col):
        number = ""

        # move left to first non-digit
        done = False
        key = f"{row},{col}"
        while key in self.map and done == False:
            temp = self.map[key]
            print( "temp", temp )
            if temp.isdigit():
                col = col - 1
                key = f"{row},{col}"
            else:
                done = True

        col = col + 1
        print( "col = ", col)

        # move right to first non-digit  
        done = False 
        key = f"{row},{col}"     
        while key in self.map and done == False:

            temp = self.map[key]
            if temp.isdigit():
                number = number + temp
                col = col + 1
                key = f"{row},{col}"
            else:
                done = True
            


        return int(number)
    

    def getPattern(self, row, col):
        pattern = ""
        a = self.map.get(f"{row-1},{col-1}", '_')
        b = self.map.get(f"{row-1},{col}", '_')
        c = self.map.get(f"{row-1},{col+1}", '_')
        d = self.map.get(f"{row},{col-1}", '_')
        e = self.map.get(f"{row},{col+1}", '_')
        f = self.map.get(f"{row+1},{col-1}", '_')
        g = self.map.get(f"{row+1},{col}", '_')
        h = self.map.get(f"{row+1},{col+1}", '_')       
        
        pattern = a+b+c+d+e+f+g+h
        
        digits = "0123456789"
        for d in digits:
            pattern = pattern.replace(d, "#")
      
        return pattern


    def oneTop(self, p):
        valid = ["#__", "##_", "_#_", "__#", "_##", "###"]
        if p[0:3] in valid:
            return True
        else:
            return False

    def oneBottom(self, p):
        valid = ["#__", "##_", "_#_", "__#", "_##", "###"]
        if p[5:] in valid:
            return True
        else:
            return False      
    
    def oneMiddle(self, p):
        valid = ["#_", "_#"]
        if p[3:5] in valid:
            return True
        else:
            return False 


    def noTop(self, p):
        if p[0:3] == "___":
            return True
        else:
            return False 

    def noBottom(self, p):
        if p[5:] == "___":
            return True
        else:
            return False 
        
    def noMiddle(self, p):
        if p[3:5] == "__":
            return True
        else:
            return False 

    def getTop(self, row, col, p):
        start = p[0:3].find("#")
        return self.findMiddle(row-1, col-1+start)
        
    def getBottom(self, row, col, p):
        start = p[5:].find("#")
        return self.findMiddle(row+1, col-1+start)
    
    def getMiddle(self, row, col, p):
        if p[3] == "#":
            return self.findMiddle(row, col-1)
        else:
            return self.findMiddle(row, col+1) 


    def findCogs(self):
        total = 0

        for key, value in self.map.items():
            if value == "*":
            # print(f"{key} = {value}")
                row, col = key.split(",")
                row = int(row)
                col = int(col)
                #print( f"row = {row}, col = {col}")

                # check for two numbers
                p = self.getPattern(row, col)


                if p == "#_#_____":
                    num1 = self.findMiddle(row-1, col+1)
                    num2 = self.findMiddle(row-1, col-1)
                    print( "two top: ", num1, num2, num1*num2 )
                    total = total + num1*num2
                elif p == "___##___":
                    num1 = self.findMiddle(row, col+1)
                    num2 = self.findMiddle(row, col-1)
                    print( "two middle: ", num1, num2, num1*num2 )
                    total = total + num1*num2
                elif p == "_____#_#":
                    num1 = self.findMiddle(row+1, col+1)
                    num2 = self.findMiddle(row+1, col-1)
                    print( "two bottom: ", num1, num2, num1*num2 )
                    total = total + num1*num2
                elif self.oneTop(p) and self.oneMiddle(p) and self.noBottom(p):
                    num1 = self.getTop(row, col, p)
                    num2 = self.getMiddle(row, col, p)
                    print("one top and one middle", num1, num2, num1*num2) 
                    total = total + num1*num2
                elif self.oneTop(p) and self.oneBottom(p) and self.noMiddle(p):
                    num1 = self.getTop(row, col, p)
                    num2 = self.getBottom(row, col, p)
                    print("one top and one bottom", num1, num2, num1*num2)
                    total = total + num1*num2 
                elif self.noTop(p) and self.oneBottom(p) and self.oneMiddle(p):
                    num1 = self.getMiddle(row, col, p)
                    num2 = self.getBottom(row, col, p)
                    print("one middle and one bottom", num1, num2, num1*num2) 
                    total = total + num1*num2     
                else:
                    print("pattern not found")


        return total

# ---- main ----
partA = Schematic()

#partA.solveA("day03/test_a.txt")
#partA.solveA("day03/a.txt")
#partA.debug()

#partA.solveB("day03/b.txt")
#partA.solveB("day03/test_a.txt")
partA.solveB("day03/a.txt")



