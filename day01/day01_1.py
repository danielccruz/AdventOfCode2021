
previous_value = 0
counter = -1

with open('AdventOfCode2021/day01/day01.input', 'r+') as f:
    for line in f.readlines():
        if int(line) > previous_value:
            counter+=1
        previous_value = int(line)
        
print('Times the depth increased: ', counter)