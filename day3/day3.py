import os
dir_path = os.path.dirname(os.path.realpath(__file__))


with open (dir_path+'/input.txt') as file:
    lines = file.readlines()


digitTable=[]
symbolTable=[[0 for i in range ( 0,  len(lines[0])+1) ]]


for i in range(0, len(lines)):
    digits=[]
    digitsLine=[]
    symbolLine=[0 for i in range ( 0,  len(lines[i])+1) ]
    lastDigitPos=-10
    firstDigitPos=-10
    wholeDigit = ''
    for j in range(0, len(lines[i])):
        if(lines[i][j].isdigit()):
            if(j+1<len(lines[i])):
                if(not lines[i][j+1].isdigit() and not lines[i][j-1].isdigit()):
                    digitsLine.append([j, j, lines[i][j], 0])
                    continue
                elif(not lines[i][j+1].isdigit() and j-1<0):
                    digitsLine.append([j, j, lines[i][j], 0])
                    continue
                elif(j+1> len(lines[i]) and lines[i][j-1].isdigit()):
                    digitsLine.append([j, j, lines[i][j], 0])
                    continue

            if(lastDigitPos+1==j and lastDigitPos>-1):
                wholeDigit+=(str(lines[i][j]))

            else:

                firstDigitPos=j

                wholeDigit=str(lines[i][j])
            lastDigitPos=j
        elif(lastDigitPos>-1):
            if not wholeDigit == -5:
                digitsLine.append([firstDigitPos, lastDigitPos, wholeDigit, 0, 0])
            wholeDigit=-5

        if(not lines[i][j].isdigit() and not lines[i][j]=='.' and not lines[i][j]=='\n'):
            symbolLine[j] = lines[i][j]
    symbolTable.append(symbolLine)

    digitTable.append(digitsLine)

sum = 0
for l in range (0, len(digitTable)):
    if digitTable[l]:
        for r in range (0, len(digitTable[l])):
            pocetak=digitTable[l][r][0]
            kraj=digitTable[l][r][1]
            lplus2=0
            lminus1=0
            if l+2>len(digitTable):
                lplus2=l+1
            else:
                lplus2=l+2
            if l-1 <0:
                lminus1=0
            else:
                lminus1=l-1
            for i in range(lminus1, lplus2):
                krajplus2=0
                pocetakminus1=0
                if l+2>len(digitTable):
                    lplus2=l+1
                else:
                    lplus2=l+2
                if l-1 <0:
                    lminus1=0
                else:
                    lminus1=l-1
                for j in range(pocetak-1, kraj+2):
                    if(not symbolTable[i+1][j]==0):

                        if (digitTable[l][r][3]==0):
                            sum+= int(digitTable[l][r][2])
                            digitTable[l][r][3]=1

print(sum)
# gearRatioSum=0
# for i in range(1, len(symbolTable)-1):
#     previous=[]
#     thisLine=[]
#     nextLine=[]
#     for j in range(0, len(symbolTable[i])):
#         candidates =[]

#         if symbolTable[i][j]=='*':
#             for item in digitTable[i-1]:
#                 if(i-2 >=0):
#                     previous = digitTable[i-2]
#                 thisLine = digitTable[i-1]
#                 nextLine = digitTable[i]
#                 print(previous, "|",  thisLine, "|", nextLine, "| prev, this, next")
#                 for item in previous:
#                     if item[0]-1 <=j<=item[1]+1:
#                         print("its in", item[2], item[0], item[1], 'prev', j)
#                         candidates.append(item[2])

#                 for item in thisLine:
#                     if item[0]-1 <=j<=item[1]+1:
#                         print("its in", item[2], item[0], item[1], 'this', j)
#                         candidates.append(item[2])


#                 for item in nextLine:
#                     if item[0]-1 <=j<=item[1]+1:
#                         print("its in", item[2], item[0], item[1], 'next', j)
#                         candidates.append(item[2])
#             print(candidates)