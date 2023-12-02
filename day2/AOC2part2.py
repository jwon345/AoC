f = open("input.txt", "r")
input = f.readlines(-1)

count = []
red = 12
green = 13
blue = 14

for i, line in enumerate(input):
    redCount = [0]
    blueCount = [0]
    greenCount = [0]

    while (line.find("red") != -1):
        index = line.find("red")
        redCount.append(int(line[index-3:index -1]))
        line = line[0:index] + line[index + 3 : len(line)]
    while (line.find("blue") != -1):
        index = line.find("blue")
        blueCount.append(int(line[index-3:index -1]))
        line = line[0:index] + line[index + 3 : len(line)]
    while (line.find("green") != -1):
        index = line.find("green")
        greenCount.append(int(line[index-3:index -1]))
        line = line[0:index] + line[index + 3 : len(line)]
    count.append(max(redCount)*max(blueCount)*max(greenCount))
print(sum(count))