import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/input.txt') as file:
    lines = file.readlines()

max=[12, 13, 14]
finalSum = 0
gamesArray=[]

def checkValidity(oneGame):
    for index in range(0, len(oneGame)):
        if(oneGame[index][0]>max[0] or oneGame[index][1]>max[1] or oneGame[index][2]>max[2]):
            return False
    return True



for i in range (0, len(lines)):
    grab = lines[i].split('\n')[0].split(': ')[1].split('; ')
    oneGame=[]

    for j in range (0, len(grab)):
        item = grab[j].split(', ')
        onePull=[0, 0, 0]
        for color in item:
            if color.endswith('red'):
                onePull[0]=int(color[:-3])
            if color.endswith('green'):
                onePull[1]=int(color[:-5])
            if color.endswith('blue'):
                onePull[2]=int(color[:-4])
        oneGame.append(onePull)
    if checkValidity(oneGame):
        finalSum+=int(i+1)
    gamesArray.append(oneGame)
print(finalSum)