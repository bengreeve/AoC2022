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

allElfs.sort(reverse=True)

top = 3
sum = 0
# loop from 0 to top
for num in range(0, top, 1):
    sum = sum + allElfs[num]

print(sum)