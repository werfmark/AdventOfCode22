import os

def RoundResult(round):
    if round[0] == 'A' and round[1] == 'X':
        return 3
    if round[0] == 'A' and round[1] == 'Y':
        return 4
    if round[0] == 'A' and round[1] == 'Z':
        return 8
    if round[0] == 'B' and round[1] == 'X':
        return 1
    if round[0] == 'B' and round[1] == 'Y':
        return 5
    if round[0] == 'B' and round[1] == 'Z':
        return 9
    if round[0] == 'C' and round[1] == 'X':
        return 2
    if round[0] == 'C' and round[1] == 'Y':
        return 6
    if round[0] == 'C' and round[1] == 'Z':
        return 7


def splitlist(lijst):
    for item in lijst:
        yield item.split()

with open(os.getcwd() + '/Day2/input.txt', 'r') as f:
    lines = f.read()

temp = lines.split('\n')
listOfRounds = list(splitlist(temp))

total = 0

for round in listOfRounds:
    total = total + RoundResult(round)

print(total)