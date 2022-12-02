# Read input
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
    
    # Add to sum the score for their choice and the result of the round
    totalScore += (ord(line[2]) - 87)
    difference = ord(line[2]) - ord(line[0])
    # If 23, both players did the same option
    if difference == 23: totalScore += 3
    # If 21, opponent did scissors and we win. If 24, they did paper or rock and we win
    elif difference == 21 or difference == 24: totalScore += 6

print(totalScore)

file.close()

