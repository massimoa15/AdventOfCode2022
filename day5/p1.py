# Read input
#file = open('example.txt','r')
file = open('input.txt','r')

# First, let's read the beginning section of the file that outlines the starting state
# This is hard coded based on my input file. There are 9 stacks so we will work accordingly
#stacks = [['Z','N'],['M','C','D'],['P']]
stacks = [['T','D','W','Z','V','P'],['L','S','W','V','F','J','D'],['Z','M','L','S','V','T','B','H'],['R','S','J'],['C','Z','B','G','F','M','L','W'],['Q','W','V','H','Z','R','G','B'],['V','J','P','C','B','D','N'],['P','T','B','Q'],['H','G','Z','R','C']]

# Let's read through the input so that we get to the instructions line

while True:
    line = file.readline()
    # If line is just a newline character, we are done the beginning portion
    if line == '\n':
        break

# Loop through input file
while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break
    
    # line isn't empty, still reading information. Need to parse line
    instructions = line.replace('move','').replace('from','').replace('to','').strip().split()

    # instructions is now a list that contains the current instructions. 
    # instructions[0] is the start location, [1] is the amount to move from that location, and [2] is where to move them to
    [amt,start,end] = instructions
    amt = int(amt)
    start = int(start)
    end = int(end)

    # Perform actions
    for i in range(amt):
        temp = stacks[start-1].pop()
        stacks[end-1].append(temp)

for stack in stacks:
    print(stack.pop())