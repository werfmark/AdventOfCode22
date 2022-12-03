from collections import Counter
import os

def ConvertLetterToValue(letter):
    if ord(letter) >= ord('a'):
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27    
    

def GetDuplicateCharacterValue(str):
    length = len(str)
    firsthalf = str[:length//2]
    lasthalf = str[length//2:]
    for letter in firsthalf:
        if letter in lasthalf:
                return(ConvertLetterToValue(letter))
    return 0

with open(os.getcwd() + '/Day3/Input.txt', 'r') as f:
    lines = f.read()

temp = lines.split('\n')

total = 0

for str in temp:
    total = total + GetDuplicateCharacterValue(str)


print(total)