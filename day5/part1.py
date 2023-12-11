f = open("input.txt" ,"r")
input = f.read(-1)
input = input.split("\n")

strSeed =input[0].split(":")[1].split()
seeds = []
seedsHandled = []
for s in strSeed:
    seeds.append(int(s))
    seedsHandled.append(0)
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
print(min(seeds))