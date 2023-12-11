f = open("day6/input.txt", "r")
input = f.readlines(-1)

times = (input[0].split()[1:])
distance = (input[1].split()[1:])
print(input)
print(times)
print(distance)

res = []

for i, t in enumerate(times):
    holder = []
    for x in range(int(t)):
       if(((int(t)-x)*x) > int(distance[i])):
            print((int(t)-x)*x)
            holder.append(x)
    res.append(holder)
print(res)
    
sum = 1
for x in res:
    sum *= len(x)
    print(len(x))
print(sum)
        