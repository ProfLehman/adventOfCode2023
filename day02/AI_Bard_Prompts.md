
## AOC Day 2 Part I - Solved using Google Bard ##

---
### Prompts used ... ###
1. Python to read file "day2.txt" with following multiple lines of the following data "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
2. read data from file "day2.txt" rather than list
3. Text file named "day2.txt" contains lines of data with format  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", show Python code needed to read and display all lines.
4. Update code to print the maximum number of blue, green, and red data items in each line.
Sure, here is the updated code:
4. Combine last result with reading lines from file "day2.txt"
5. Text file named "day2.txt" contains lines of data with format  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", show Python code needed to read and display all lines showing the maximum number of blue, green, and red data items in each line.
Sure, here's the Python code to read the lines from the file "day2.txt" and display the maximum number of blue, green, and red data items in each line:
6. Text file named "day2.txt" contains lines of data with format  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", show Python code needed to read and display all lines showing the maximum red, maximum blue, and maximum green for each line.
Sure, here is the updated code:
7. This code will read the lines from the file "day2.txt" and process each line to count the occurrences of each color (red, blue, green). Then, it will find the maximum count for each color and print it along with the corresponding line.
8. Text file named "day2.txt" contains lines of data with format  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue". The number of each color precedes the color.  "2 green" indicates two green. Show Python code needed to read and display all lines showing the maximum red, maximum blue, and maximum green for each line.
Sure, here's the Python code to read the lines from the file "day2.txt" and process each line to count the occurrences of each color (red, blue, green). Then, it will find the maximum count for each color and print it along with the corresponding line:
9. Update to display rows if max red <= 12, max green <= 13, and max blue <= 14
10. This code first defines the maximum limits for each color. Then, it processes each line, extracting the color information and keeping track of the maximum counts for each color. If the line meets the maximum color limits, it is added to a list of filtered lines. Finally, the filtered lines are printed along with the maximum counts for each color.
11. print a sum of the filtered lines game numbers
Sure! The sum of game IDs: 2
12. This code first defines the maximum limits for each color. Then, it processes each line, extracting the color information and keeping track of the maximum counts for each color. If the line meets the maximum color limits, it is added to a list of filtered lines. Finally, the filtered lines are printed along with the maximum counts for each color.  Print the sum of the filtered lines game number.

---
### Final Code Version - Solves Day 02 - Part I ###
[day2a_AI.py](day2a_AI.py) day 2 solution generated completly by Google Bard AI)
---

```
{
import re

# Regular expression pattern to extract color information
pattern = r"(\d+) (\w+)"

# Define the maximum limits for each color
max_red = 12
max_green = 13
max_blue = 14

# Read the data from the file
with open("day2.txt", "r") as f:
    data = f.read()

# Split the data into lines
lines = data.split("\n")

# Process and filter lines
filtered_lines = []
game_ids = []

for line in lines:
    # Initialize counters for each color
    red_max = 0
    blue_max = 0
    green_max = 0

    # Extract game ID and color information
    game_id = int(line.split(":")[0].split("Game ")[-1])
    for match in re.finditer(pattern, line):
        count = int(match.group(1))
        color = match.group(2)

        if color == "red":
            if count > red_max:
                red_max = count
        elif color == "blue":
            if count > blue_max:
                blue_max = count
        elif color == "green":
            if count > green_max:
                green_max = count

    # Check if the line meets the maximum color limits and add game ID
    if red_max <= max_red and green_max <= max_green and blue_max <= max_blue:
        filtered_lines.append(line)
        game_ids.append(game_id)

# Calculate and print the sum of game IDs
sum_game_ids = sum(game_ids)

# Print the filtered lines and the maximum counts for each color
for line in filtered_lines:
    # Initialize counters for each color
    red_max = 0
    blue_max = 0
    green_max = 0

    # Extract color information using regular expression
    for match in re.finditer(pattern, line):
        count = int(match.group(1))
        color = match.group(2)

        if color == "red":
            if count > red_max:
                red_max = count
        elif color == "blue":
            if count > blue_max:
                blue_max = count
        elif color == "green":
            if count > green_max:
                green_max = count

    # Print the line and the maximum counts for each color
    print(f"{line} | Maximum Red: {red_max} | Maximum Blue: {blue_max} | Maximum Green: {green_max}")

# Print the sum of game IDs
print(f"\nSum of Game IDs: {sum_game_ids}")
}
```
---
