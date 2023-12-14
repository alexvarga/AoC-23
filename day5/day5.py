# from tqdm import tqdm

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import re
with open(dir_path+'/test.txt', 'r') as file:
    lines = file.readlines()

sts=0
stf=0
ftw=0
wtl=0
ltt=0
tth=0
htl=0

seedToSoil=[]
soilToFertilizer=[]
fertilizerToWater=[]
waterToLight=[]
lightToTemperature=[]
temperatureToHumidity=[]
humidityToLocation=[]

loopy = [seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]

seeds=[]
largestSeed=0
smallestSeed=0





for line in lines:
    if 'seeds:' in line:
        seeds= line.split(':')[1].split()

    if 'seed-to-soil map:' in line:
        sts=1
        continue
    if sts==1:
        if(len(line.split())>0):
            seedToSoil.append(line.split())
    if line == "\n":
        sts=0

    if 'soil-to-fertilizer map:' in line:
        stf=1
        continue
    if stf==1:
        if(len(line.split())>0):
            soilToFertilizer.append(line.split())
    if line == "\n":
        stf=0

    if 'fertilizer-to-water map:' in line:
        ftw=1
        continue
    if ftw==1:
        if(len(line.split())>0):
            fertilizerToWater.append(line.split())
    if line == "\n":
        ftw=0

    if 'water-to-light map:' in line:
        wtl=1
        continue
    if wtl==1:
        if(len(line.split())>0):
            waterToLight.append(line.split())
    if line == "\n":
        wtl=0

    if 'light-to-temperature map:' in line:
        ltt=1
        continue
    if ltt==1:
        if(len(line.split())>0):
            lightToTemperature.append(line.split())
    if line == "\n":
        ltt=0

    if 'temperature-to-humidity map:' in line:
        tth=1
        continue
    if tth==1:
        if(len(line.split())>0):
            temperatureToHumidity.append(line.split())
    if line == "\n":
        tth=0

    if 'humidity-to-location map:' in line:
        htl=1
        continue
    if htl==1:
        if(len(line.split())>0):
            humidityToLocation.append(line.split())
    if line == "\n":
        htl=0

smallestLocation = 0 # special case
largestLocation = 0
smallestLocation=int(humidityToLocation[0][1])
smallestRange = int(humidityToLocation[0][2])
for item in humidityToLocation:
    if smallestLocation>int(item[1]) and int(item[1])>0:
        smallestLocation=int(item[1])
        smallestRange = int(item[2])


for item in humidityToLocation:
    if int(largestLocation)<int(item[1]) and int(item[1])>0:
        largestLocation=int(item[1])






def findLocation(inputs, map):
    dests = []
    for seed in inputs:
        s = int(seed)

        for item in map:
            if s>=int(item[1]) and s<int(item[1])+int(item[2]):
                dest = s+(int(item[0]) - int(item[1]) )
                break
            else:
                dest=s

        dests.append(dest)
    return(dests)

a = []

seedss = set()
seedsStart = seeds[::2]
seedsRange = seeds[1::2]
seedEnd = []
for sss in range(0, len(seedsStart)):
    seedEnd.append(int(seedsStart[sss])+int(seedsRange[sss]))


for ss in seedEnd:
    s=int(ss)
    if s>largestSeed:
        largestSeed=s

smallestSeed=seedsStart[0]
for ss in seedsStart:
    if ss<smallestSeed:
        smallestSeed=ss
for i in range(0, len(seedsStart)):
    for s in range(0, int(seedsRange[i])):
        seedss.add(int(seedsStart[i])+s)



for i in loopy:

    seedss = findLocation(seedss, i)

def findSeed(inputs, map):
    origins = []
    for seed in inputs:
        s = int(seed)

        for item in map:
            if s>=int(item[0]) and s<int(item[0])+int(item[2]):
                origin = s+(int(item[1]) - int(item[0]) )
                break
            else:
                origin=s

        origins.append(origin)
    return(origins)

# a = findSeed(inputs, humidityToLocation)
# print(a, "AAA")
# b = findSeed(a, temperatureToHumidity)
# print(b, "bbb")
wantedSeed = 0

for ls in range(0, smallestLocation+smallestRange ):
# for ls in tqdm(range(0, smallestLocation )):
    inputs=[ls]
    for l in reversed(loopy):
        inputs=findSeed(inputs, l)
    # print(inputs, "--", ls, l, 'loopy')

    for i in range(0, len(seedsStart)):
        if inputs[0] in range(int(seedsStart[i]), int(seedsStart[i])+ int(seedsRange[i])):
            wantedSeed = ls
            print(inputs[0], ls)
            break
    if(wantedSeed!=0):
        break