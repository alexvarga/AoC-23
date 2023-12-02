
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import re
sum = 0
with open(dir_path+'/input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e').replace('zero', 'z0o')
    line = re.sub("[^0-9]", "", line)
    if len(line)<2:
        line = line+line
        sum+=int(line)
    elif len(line)>2:
        line = line[0]+line[-1]
        sum+=int(line)
    else:
        sum+=int(line)

print(sum)
