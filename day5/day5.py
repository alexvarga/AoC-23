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


for i in range(0, len(seedsStart)):
    for s in range(0, int(seedsRange[i])):
        seedss.add(int(seedsStart[i])+s)


print(len(seedss))

for i in loopy:

    seedss = findLocation(seedss, i)

print(min(seedss), "min destination")
