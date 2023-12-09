import os
dir_path = os.path.dirname(os.path.realpath(__file__))

coords = set()

with open (dir_path+'/input.txt') as file:
    grid = file.readlines()


starPositions = []
# print(lines)

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == '.':
            continue
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if(cr<0 or cr>=len(grid) or cc<0 or cc>=len(grid[cr]) or not grid[cr][cc].isdigit()):
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc-=1
                coords.add((cr, cc))

# print(coords)

numbers = []

for r,c in coords:
    num=''
    while grid[r][c].isdigit() and c<len(grid[r]):
        num+=grid[r][c]
        c+=1
    numbers.append(int(num))

# print(numbers)
print(sum(numbers))



numbers = []
total = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue
        cs = set()

        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if(cr<0 or cr>=len(grid) or cc<0 or cc>=len(grid[cr]) or not grid[cr][cc].isdigit()):
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc-=1
                cs.add((cr, cc))

        if len(cs)!=2:
            continue

        numbers = []

        for cr,cc in cs:
            num=''
            while grid[cr][cc].isdigit() and cc<len(grid[cr]):
                num+=grid[cr][cc]
                cc+=1
            numbers.append(int(num))

        total +=numbers[0]*numbers[1]

print(total)