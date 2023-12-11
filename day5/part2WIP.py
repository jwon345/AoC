f = open("day5/iinput.txt" ,"r")
input = f.read(-1)
input = input.split("\n")

strSeed =input[0].split(":")[1].split()
print(strSeed)
seedStart = strSeed[0:len(strSeed):2]
lengthStr = strSeed[1:len(strSeed):2]
length = []
seeds = []
for i,seed in enumerate(seedStart):
    seeds.append((int(seed), int(seed) + int(lengthStr[i])))
print(length)

print("xxxx")
# seedsHandled = []
# for i,val  in enumerate(seedStart):
#     for j in range(1,length[int(i)],1):
#         seeds.append(int(val)+j)
#         seedsHandled.append(0)
#         print(int(val)+j)
print("asdf")
print(seeds)
holder = seeds
stage = 0

split = seeds

for i, line in enumerate(input):
    if len(line) == 0:
        continue
    elif line.split()[1] == "map:":
        print("\n\n")
        seeds = holder
        holder = []
        print("new seeds")
        print(seeds)

        # for i in range(0,len(seedsHandled),1):
        #     seedsHandled[i] = False
        stage += 1 
        continue
    elif len(line.split()) == 3:
        print(line)
        dest, source, step = line.split()
        dest = int(dest)
        source = int(source)
        step = int(step)
        for j, seed in enumerate(seeds):
                if seed[0] >= source  and seed[1] <= source + step:
                    newSeed = (seed[0]+ dest-source, seed[1] + dest-source)
                    holder.append(newSeed)
                    print(str(seed)+ " -all-> " + str(newSeed))

                if seed[0] >= source  and seed[1] > source + step:
                    newSeed = (seed[0]+ dest-source, dest)
                    holder.append(newSeed)
                    print(str(seed)+ " -left-> " + str(newSeed))

                if seed[0] < source  and seed[1] > source and seed[1] <= source + step:
                    newSeed = (source, seed[1] + dest-source)
                    holder.append(newSeed)
                    print(str(seed)+ " -right-> " + str(newSeed))

                
print(seeds)
print(min(seeds))