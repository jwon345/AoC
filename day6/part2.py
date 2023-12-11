import time

f = open("day6/input.txt", "r")
input = f.readlines(-1)

startTime = time.time()


timesX = (input[0].split()[1:])
distanceX = (input[1].split()[1:])
t = ""
distance = ""
for x in timesX:
    t = t + x

for x in distanceX:
    distance = distance + x

print(input)
print(distance)

res = []

holder = []
for x in range(int(t)):
    if(((int(t)-x)*x) > int(distance)):
        # print((int(t)-x)*x)
        holder.append(x)
res.append(holder)
# print(res)
    
sum = 1
for x in res:
    sum *= len(x)
    # print(len(x))
print(sum)
print("Day 6 Part 2 time = " + str(time.time() - startTime) + "s")
        