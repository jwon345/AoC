f = open("input.txt", "r")
input = f.readlines(-1)

count = []
red = 12
green = 13
blue = 14

for i, line in enumerate(input):
    cRed = True 
    cGreen = True
    cBlue = True

    while (line.find("red") != -1):
        index = line.find("red")
        redSum = int(line[index-3:index -1])
        if redSum > red:
            cRed = False
        line = line[0:index] + line[index + 3 : -1]
    while (line.find("blue") != -1):
        index = line.find("blue")
        blueSum = int(line[index-3:index -1])
        if blueSum > blue:
            cBlue = False
        line = line[0:index] + line[index + 3 : -1]
    while (line.find("green") != -1):
        index = line.find("green")
        greenSum = int(line[index-3:index -1])
        if greenSum > green:
            cGreen = False
        line = line[0:index] + line[index + 3 : -1]
    if (cRed and (cGreen and cBlue)):
        count.append(i+1)
print(sum(count))