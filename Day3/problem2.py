import os

def ConvertLetterToValue(letter):
    if ord(letter) >= ord('a'):
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27    

def GetDuplicateCharacterValue(strOne, strTwo,strThree):
    for letter in strOne:
        if letter in strTwo:
                if letter in strThree:
                    return(ConvertLetterToValue(letter))
    return 0

with open(os.getcwd() + '/Day3/Input.txt', 'r') as f:
    lines = f.read()

temp = lines.split('\n')

listByThree = list(zip(temp[0::3], temp[1::3], temp[2::3]))

total = 0

for subList in listByThree:
    total += GetDuplicateCharacterValue(subList[0], subList[1],subList[2])

print(total)
