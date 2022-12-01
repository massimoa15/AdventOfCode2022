# Read input
file = open('input.txt','r')

# Count the elf's calories
counter = 0

# Current highest calorie count
largest = 0

while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break

    # If newline, we're done with the current elf
    if line == '\n':
        if counter > largest: largest = counter
        counter = 0
        continue
    counter += int(line)

print(largest)