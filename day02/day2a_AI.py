import re

# Regular expression pattern to extract color information
pattern = r"(\d+) (\w+)"

# Define the maximum limits for each color
max_red = 12
max_green = 13
max_blue = 14

# Read the data from the file
with open("day02/day2.txt", "r") as f:
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
