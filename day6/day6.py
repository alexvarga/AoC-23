import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/input.txt', 'r') as file:
    lines = file.read()

time= lines.split('\n')[0].split(':')[1].split()
distances= lines.split('\n')[1].split(':')[1].split()

print(time)
print(distances)
results = []
result = 1
for i in range(0, len(time)):
    outcomes =[]

    for j in range(1, int(time[i])):
        outcomes.append(j*(int(time[i])-j))


    wins=len([item for item in outcomes if item > int(distances[i])])
    results.append(wins)
    result = result * wins

print(result)