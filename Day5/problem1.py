import os
import numpy as np

stackheigth = 0
stackwidth = 0
stacks = list()
moves = list()

def CreateStacks():
    for x in range(stackheight):
        stacks.append(list([inputlist[x][1::4]]))

def RemoveEmptyFromStacks(stacks):
    for stack in stacks:
        while('' in stack):
            stack.Remove('')

def SetStackDimensions(inputlist):
    for i in range(len(inputlist)):
        if inputlist[i][1] == '1':
            global stackheight
            stackheight = i
            global stackwidth
            stackwidth = inputlist[i][-2]
            break

def SetMoves(inputlist):
    for x in inputlist[(stackheight+2):]:
        m = x.split()
        li = list(map(int, m[1::2]))
        moves.append(li)
        
with open(os.getcwd() + '/Day5/exampleInput.txt', 'r') as f:
    lines = f.read()

inputlist = lines.split('\n')

SetStackDimensions(inputlist)
CreateStacks()
print(stacks)
stack2 = list()
for s in zip(*stacks):
    stack2.append(s)
print(stack2)

RemoveEmptyFromStacks(stacks)
SetMoves(inputlist)

print(stacks)
print(moves)







