import os

with open(os.getcwd() + '/Day4/Input.txt', 'r') as f:
    lines = f.read()

temp = lines.split('\n')


def SplitToInt(str):
    l = str.split(',')
    first = list(map(int, l[0].split('-')))
    latter = list(map(int,l[1].split('-')))
    return first + latter

def Contained(listOfInts):
    if listOfInts[0] >= listOfInts[2] and listOfInts[1]<= listOfInts[3]:
        return 1
    if listOfInts[2] >= listOfInts[0] and listOfInts[3]<= listOfInts[1]:
        return 1
    return 0        
        
total = 0

for str in temp:
    total += Contained(SplitToInt(str))

print(total)