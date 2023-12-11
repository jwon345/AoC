import time
start = time.time()
f = open("day5/input.txt" ,"r")
input = f.read(-1)
input = input.split("\n")

strSeed =input[0].split(":")[1].split()

startSeed = strSeed[0:len(strSeed):2]
lenSeed = strSeed[1:len(strSeed):2]

print(strSeed)
print(startSeed)
print(lenSeed)

seeds = []
seedsHandled = []

for initSeed in startSeed:
    for steps in lenSeed:
        for i in range(0,int(steps),1):
            seeds.append(int(initSeed)+i)
            seedsHandled.append(0)

# for s in strSeed:
#     seeds.append(int(s))
stage = 0
for i, line in enumerate(input):
    if len(line) == 0:
        continue
    elif line.split()[1] == "map:":
        print("\n\n")
        print(seeds)
        for i in range(0,len(seedsHandled),1):
            seedsHandled[i] = False
        stage += 1 
        continue
    elif len(line.split()) == 3:
        print(line)
        dest, source, step = line.split()
        for j, seed in enumerate(seeds):
            if seed in (range(int(source),int(source)+int(step),1)):
                if (seedsHandled[j] == False):
                    print("---"+str(seed) + " + " + str(int(dest)-int(source)))
                    print("thing is " + str(j))
                    seeds[j] = seeds[j] + (int(dest)-int(source))
                    seedsHandled[j] = True 
                
print(seeds)
print("time = " + str(time.time()-start) + "Seconds")
print(min(seeds))