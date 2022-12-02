## Advent of Code
## Day 2

f = open("inputDayTwo.txt", "r")
input = f.read()

#A = Rock
#B = Paper
#C = Scissor

#x = lose
#y = tie
#Z = win

totalpoints = 0

losesTo = {
    "A" : "C",
    "B" : "A",
    "C" : "B",
}

winsFrom = {
    "C" : "A",
    "A" : "B",
    "B" : "C",
}

lines = input.split('\n') 
for line in lines:

    matchPoints = 0

    line = line.split(" ")

    opponentChoice = line[0]

    match line[1]:
        
        case "X":
            myChoice = losesTo[opponentChoice]

        case "Y":
            matchPoints = matchPoints + 3
            myChoice = opponentChoice

        case "Z":
            myChoice = winsFrom[opponentChoice]
            matchPoints = matchPoints + 6 

    match myChoice:
            case "A":
                matchPoints = matchPoints + 1
            case "B":
                matchPoints = matchPoints + 2
            case "C":
                matchPoints = matchPoints + 3
    
    totalpoints = totalpoints + matchPoints

print(totalpoints)