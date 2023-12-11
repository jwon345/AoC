import time
startTime = time.time()
f = open("input.txt", "r")
# f = open("iinput.txt", "r")
input = f.readlines(-1)

multiplier = []
for i in range(0,len(input)):
    multiplier.append(1)
total = []
for i,line in enumerate(input):
    line = line.replace("\n", "")
    power = []
    card = line.split(":")[1]
    lhs, rhs = card.split("|")
    lhs = lhs.split()
    rhs = rhs.split()
    #print(lhs)
    # #print(rhs)
    count = 1
    for winningCard in lhs:
        if winningCard in rhs:
            try:
                #print("win card" + str(i + count + 1))
                multiplier[i + count] += 1*multiplier[i]
                count += 1
                ##print(winningCard)
            except:
                pass
##print(total)
# print(sum(total))
print(sum(multiplier))
print("Part 2 time = " + str(time.time() - startTime) + "s")
 