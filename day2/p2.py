# Read input
#file = open('example.txt','r')
file = open('input.txt','r')

# To count the score as we go
totalScore = 0

# Loop through input file
while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break

    # Not end of file, determine points for this round
    tempScore = 0
    # Add to sum the score for the result of the round
    tempScore += (ord(line[2]) - 88) * 3
    # Determine point for their choice

    # Draw, points equal to the opponents value
    if line[2] == 'Y': tempScore += ord(line[0]) - 64
    # Win, determine what you chose
    elif line[2] == 'Z': 
        # temp will be 0 if rock, 1 if paper, 2 if scissors (from opponent)
        temp = ord(line[0]) - 63
        # in the case of a victory, you need to increase temp by 1. If they threw scissors then we need to loop back to rock as our choice (modulo)
        if temp == 4: temp = 1
        tempScore += temp
    # Loss, determine what you chose
    else:
        temp = ord(line[0]) - 65
        if temp == 0: temp = 3
        tempScore += temp

    totalScore += tempScore
    #print(tempScore)

print(totalScore)

file.close()

