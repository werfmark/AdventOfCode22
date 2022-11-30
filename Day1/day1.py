print('dit is dag1oplssing')

array = [199,200,208,210,200,207,240,269,260,263]

print(array[1])

increases = 0

for index, value in enumerate(array[0:9]):
    if array[index] > array[index-1]:
        increases += 1

print(increases)