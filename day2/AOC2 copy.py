f = open("input.txt", "r")
input = f.readlines(-1)

count = []
a = {
"red" : 12,
"green" : 13,
"blue" : 14
}


sum = 0
for i, line in enumerate(input):
    cRed = True 
    cGreen = True
    cBlue = True
    id, Data = line.split(":")
    print(Data)
    idd = (id.split(" ")[1])
    canPass = True
    for unit1 in Data.split(";"):   
        for unit2 in unit1.split(","):   
            unit = unit2.split(" ")
            if int(unit[1]) > a[unit[2].replace("\n", "")]:
                canPass = False
    if canPass:
        sum += int(idd)        
print(sum)