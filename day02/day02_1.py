
x,y = 0,0

with open('AdventOfCode2021/day02/day02.input', 'r+') as f:
    for line in f.readlines():
        move, value = line.strip().split(' ')
        if move == 'forward':
            y+= int(value)
        elif move == 'down':
            x+= int(value)
        elif move == 'up':
            x-= int(value)
            
print('Horizontal position: ', y, 'Depth: ', x, 'Multiplication: ', x*y)