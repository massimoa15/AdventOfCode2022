# Read input
#file = open('example.txt','r')
file = open('input.txt','r')
file2 = open('test.txt','w')

# counter
counter = 0

# Loop through input file
while True:
    line = file.readline()
    # If line is empty, end of file, break
    if not line:
        break

    # Convert the line into numbers that can be compared. The format for this line is `d+-d+`
    [x,y] = line.strip().split(",")
    # split x and y into parts 1 and 2, split by '-'
    [x1,x2] = x.split("-")
    [y1,y2] = y.split("-")

    # Convert x1,x2,y1,y2 to int
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if (x1 >= y1 and x1 <= y2) or (x2 >= y1 and x2 <= y2) or (y1 >= x1 and y1 <= x2) or (y2 >= x1 and y2 <= x2):
        counter += 1

print(counter)
