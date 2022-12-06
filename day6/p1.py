def IsListUnique(list):
    for x in range(len(list)):
        for y in list[x+1:]:
            if list[x] == y: return False
    return True

# Read input
#file = open('example.txt','r')
file = open('input.txt','r')

# Get the input buffer
buffer = file.readline()

# Our current position offset from the start of the list
offset = 0

while True:
    # Get 4 char buffer
    temp = buffer[offset:offset+4]

    # Check if unique. If yes, we're done
    if IsListUnique(temp): break

    # Not unique, move forward
    offset += 1

print(offset+4)