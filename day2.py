## Advent of Code
## Day 2

f = open("inputDayTwo.txt", "r")
input = f.read()
input = input.replace("X", "A").replace("Y", "B").replace("Z", "C")

#A = Rock
#B = Paper
#C = Scissor

totalpoints = 0

lines = input.split('\n') 
for line in lines:

    matchPoints = 0

    line = line.split(" ")

    match line[1]:
        case "A":
            matchPoints = matchPoints + 1
        case "B":
            matchPoints = matchPoints + 2
        case "C":
            matchPoints = matchPoints + 3

    if line[0] == line[1]:
        matchPoints = matchPoints + 3

    elif line[1] == "A":
        if line[0] == "C":
            matchPoints = matchPoints + 6
    elif line[1] == "B":
        if line[0] == "A":
            matchPoints = matchPoints + 6
    elif line[1] == "C":
        if line[0] == "B":
            matchPoints = matchPoints + 6

    totalpoints = totalpoints + matchPoints

print(totalpoints)      
        



