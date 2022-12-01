## Advent of Code
## Day 1

f = open("inputDayOne.txt", "r")
input = f.read()

lines = input.split('\n') 
#print(lines)

allElfs = []
elfCalories = 0
for line in lines:
    
    if line == '':
        allElfs.append(elfCalories)
        elfCalories = 0
    else:
        elfCalories = elfCalories + int(line)

print(max(allElfs))