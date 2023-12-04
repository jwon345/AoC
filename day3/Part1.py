import time
start = time.time()
f = open("input.txt", "r")
# input = f.readlines(-1)
input = f.read(-1)


listVal = []

input = input.split("\n")
# for a in input:
#     #print(a)

symbol = ['*', '/', '=', '%', '@', '&', '$', '+', '-', '#']
#print(input[len(input)-1])
#print(input)
for lineNumber, line  in enumerate(input):
    for s in symbol:
        line = line.replace(s,".")
    #print(line)
    linesplit = line.split(".")
    #print(linesplit)
    # #print(input[lineNumber])
    for i, val in enumerate(linesplit):
        # if len(val) > 1:
        #     for char in val:
        #         if 
        # sanVal = []
        # for d in val:
        #     if d.isdigit():
        #         sanVal.append(d)
        # if sanVal == []:
        #     continue
        # # #print(sanVal[0:len(sanVal)])
        # strVal = ""
        # for c in sanVal:
        #     strVal += c
        # val = strVal
        if val.isdigit():
            index = line.find(val)
            #print("get " + val +" " +str(range(index,index+len(val))))
            line = line[0:index] + len(val)*"." + line[index+len(val):len(line)]
            #print(line)
            notAdded = True
            ll1 = []
            ll2 = []
            ll3 = []
            x = 1
            if index == 0:
                x = 0
            # for j in range(index - x,len(val)+1):
            for j in range(index-1,min(len(input[lineNumber]),(index + len(val)+1)), 1):
                # #print(check)
                if not(lineNumber == 0):
                    check = input[lineNumber-1][j]
                    ll1.append(check)
                    if (not check.isdigit() and not (check == ".")):
                        if notAdded:
                            notAdded = False
                            #print("added")
                            listVal.append(int(val))

                check = input[lineNumber][j]
                ll2.append(check)
                if (not check.isdigit() and not (check == ".")):
                    if notAdded:
                        notAdded = False
                        #print("added")
                        listVal.append(int(val))

                if lineNumber < len(input) - 2:
                    check = input[lineNumber+1][j]
                    ll3.append(check)
                    if (not check.isdigit() and not (check == ".")):
                        if notAdded:
                            notAdded = False
                            #print("added")
                            listVal.append(int(val))
            #print(ll1)
            #print(ll2)
            #print(ll3)
            #print("\n")
#print(listVal) 
print(sum(listVal)) 
print("Part 1 time = " + str(time.time()-start) + "s")
    # for unit in linesplit:
    #     #print(unit) 