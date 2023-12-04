import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import re
sum = 0
with open(dir_path+'/input.txt', 'r') as file:
    lines = file.readlines()

myNums=[]
winNums=[]
winPoints=[]

for line in lines:
    a = line.split(": ")[1].split(" | ")[0]
    myNums.append(a.split())
    b= line.split(": ")[1].split(" | ")[1]
    winNums.append(b.split())


wins=[]
for i, numLine in enumerate(myNums):
    win=-1
    for num in numLine:
        if num in winNums[i]:
            win+=1
    if(win>=0):
        wins.append(win)


output=0
for i in wins:
    output+=(pow(2, i))

print(output)