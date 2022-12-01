# Read input
file = open('input.txt','r')

# Count the elf's calories
counter = 0

# Current highest calorie count
largest = [0,0,0]

while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break

    # If newline, we're done with the current elf
    if line == '\n':
        if counter > largest[0]: largest[0] = counter
        # Sort largest
        largest.sort()

        counter = 0
        continue
    counter += int(line)

print(largest)
print(largest[0] + largest[1] + largest[2])
