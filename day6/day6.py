import os
from tqdm import tqdm
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/input.txt', 'r') as file:
    lines = file.read()

time= lines.split('\n')[0].split(':')[1].replace(" ", "")
distances= lines.split('\n')[1].split(':')[1].replace(" ", "")

print(time)
print(distances)
results = []
result = 1
# for i in range(0, len(time)):
outcomes =[]

for j in tqdm(range(1, int(time))):

    # print(j)
    outcomes.append(j*(int(time)-j))


wins=len([item for item in tqdm(outcomes) if item > int(distances)])
results.append(wins)
result = result * wins

print(result)