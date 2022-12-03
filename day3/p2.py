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
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    # If line is empty, end of file, break
    if not line1:
        break

    # convert to list of chars
    list1 = list(line1)
    list2 = list(line2)
    list3 = list(line3)

    # Loop through list1 and find the character that appears in the other two lists as well
    for x in list1:
        if x in list2 and x in list3:
            priorityCounter += GetPriority(x)
            break

print(priorityCounter)
