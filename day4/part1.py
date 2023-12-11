import time
startTime = time.time()
f = open("input.txt", "r")
# f = open("iinput.txt", "r")
input = f.readlines(-1)

total = []
for line in input:
    line = line.replace("\n", "")
    power = -1
    card = line.split(":")[1]
    lhs, rhs = card.split("|")
    lhs = lhs.split()
    rhs = rhs.split()
    #print(lhs)
    #print(rhs)
    for winningCard in lhs:
        if winningCard in rhs:
            power += 1
            #print(winningCard)
    if power != -1:
        total.append(2**power)
#print(total)
print(sum(total))
print("Part 1 time = " + str(time.time() - startTime) + "s")

 