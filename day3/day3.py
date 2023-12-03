import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# import re

digitTable=[]
symbolTable=[]

# * / = + % @ # & - $
with open (dir_path+'/test.txt') as file:
    lines = file.readlines()

#for every line find numbers positions
#for every line find non dot, non number positions

#go trough numbers with their length +-1 rectange and check if symbol could be found in that rectangle
for i in range(0, len(lines)):
    # pattern = re.compile(r'^[^\.*]')
    # matches = pattern.finditer(line)
    # mo = re.search(r'\d+', line)
    # positions = [match.start() for match in matches]

    # print(mo)\
    digits=[]
    digitsLine=[]
    symbolLine=[]
    lastDigitPos=-10
    firstDigitPos=-10
    wholeDigit = ''
    for j in range(0, len(lines[i])):
        if(lines[i][j]=='\n'):
            continue
        if(lines[i][j].isdigit()):
            # print('digit', i, j)
            if(lastDigitPos+1==j and lastDigitPos>-1):
                wholeDigit+=(str(lines[i][j]))
            else:
                firstDigitPos=j
                wholeDigit=str(lines[i][j])
            lastDigitPos=j
        elif(lastDigitPos>-1):
            if not wholeDigit == -5:
                # print(wholeDigit, firstDigitPos, lastDigitPos)
                digitsLine.append([firstDigitPos, lastDigitPos, wholeDigit])
            wholeDigit=-5
    # print(digitsLine)
    digitTable.append(digitsLine)

# print(digitTable)

# print(digitTable[0][0])


    # if(mo):
    #     print(mo.span(), mo.group())