
f = open("input.txt", "r")
input = f.readlines(-1)
counter = []
for line in input:
    msd = -1
    lsd = -1 
    lineLen = len(line) - 1
    if lineLen > 1:
        for i in range(0,int(lineLen+1)):
            if msd == -1:
                if line[i].isdigit():
                    msd = i
            if lsd == -1:
                if line[lineLen - i].isdigit():
                    lsd = lineLen - i
            if (msd != -1 and lsd != -1):
                break

    else:
        msd,lsd = 0
    counter.append(int(str(line[msd]) + str(line[lsd])))
print(sum(counter))

# input = [
# "two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen",
# ]
nums = {
    1 : "one",
    2 : "two", 
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven", 
    8 : "eight", 
    9 : "nine"
}

counter = []
for line in input:
    tempLineL = ""
    tempLineR = ""
    lineLength = len(line)
    for i in range(0,lineLength):
        tempLineL += line[i]
        tempLineR = line[lineLength-1-i] + tempLineR
        for n in nums:
            tempLineL = str(tempLineL).replace(nums[n],str(n))
            tempLineR = str(tempLineR).replace(nums[n],str(n)) 
    line = tempLineL + tempLineR
    print(line)
    msd = -1
    lsd = -1 
    lineLen = len(line) - 1
    if lineLen > 1:
        for i in range(0,int(lineLen+1)):
            if msd == -1:
                if line[i].isdigit():
                    msd = i
            if lsd == -1:
                if line[lineLen - i].isdigit():
                    lsd = lineLen - i
            if (msd != -1 and lsd != -1):
                break

    else:
        msd,lsd = 0
    counter.append(int(str(line[msd]) + str(line[lsd])))
print(sum(counter))