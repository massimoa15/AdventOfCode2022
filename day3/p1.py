def GetPriority(x):
    o = ord(x)
    # If a capital letter, subtract by the offset in the ASCII table so that we can convert A to 27, B to 28, etc. This is -65 (turns A to 0) and then plus 27, which is the same as -38
    if o < 91: return o - 38
    # If a lower case letter, do the same operations on the ASCII decimal value but for lowercase instead. This equates to -96
    if o >= 97: return o - 96
    return 0

# Read input
#file = open('example.txt','r')
file = open('input.txt','r')

# counter
priorityCounter = 0

# Loop through input file
while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break

    # convert to list of chars
    fullList = list(line)

    # Split list into 2 halves
    half_length = len(fullList) // 2
    first_half, second_half = fullList[:half_length], fullList[half_length:]

    # Loop through first_half and see which character in the first half is in the second half
    for x in first_half:
        if x in second_half: 
            priorityCounter += GetPriority(x)
            break

print(priorityCounter)
