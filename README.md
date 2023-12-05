# adventOfCode2023
**[Advent of Code 2023](https://adventofcode.com/)**


Testing: GitHub Codespaces with Python, 
committing code to GithHub (ie. this repository)

## Day 1: Trebuchet (Searching Strings)

1. Part I search for first and last occurance of digit 1, 2, 3, ... 9 in string
2. Part II extends search to include digit names "one", "two", etc.
3. Note: "gotcha" must account for overlapping digit names ie. twoone => 21

## Day 2: Cube Conundrum (Split Strings)
1. Part I split string by ; , and " " to create totals for "5 red, 6 green, 7 blue" cubes
2. Part II modified totals with minimal change to Part I.
3. note: AI "gotcha" autofilled red, green, and blue counts in RBG order rather then RGB
4. AI is able to generate accurate description of code written (see comments in [day2a.py](/day02/day2a.py))
5. After completing Day 2, went back and used Google Bard AI to generate [entire solution](day02/AI_Bard_Prompts.md) for Part I.

## Day 3: Gear Ratios (Grid processing sparse array)
1. Part I add all numbers in grid that are next two a special symbol
2. Part II determine "gears" ie. "*" symbol with exactly two numbers adjacent
3. Uses logic from game of life to check x8 surrounding tiles
4. Uses Python class approach
5. Uses dictionaries

## Day 4: Scratchcards (List processing)
1. Part I. find numbers in my list that appear in winning list
2. Part II. updated future counts in list calculating additional values
3. note: key concept is to calulate future values rather than creating additional card instances throug brute force

## day 5: ?
