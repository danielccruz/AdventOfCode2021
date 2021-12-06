gamma = ''
epsilon = ''
occurences_counter = []

with open('AdventOfCode2021/day03/day03.input', 'r+') as f:
    line = f.readline().strip()
    occurences_counter = [(0,0) for _ in range(0,len(line))]

    for i in range(0, len(line)):
        if line[i] == '0':
            occurences_counter[i] = (occurences_counter[i][0]+1,(occurences_counter[i][1]))
        else:
            occurences_counter[i] = (occurences_counter[i][0],(occurences_counter[i][1]+1))

    for line in f.readlines():
        line = line.strip()
        for i in range(0, len(line)):
            if line[i] == '0':
               occurences_counter[i] = (occurences_counter[i][0]+1,(occurences_counter[i][1]))
            else:
               occurences_counter[i] = (occurences_counter[i][0],(occurences_counter[i][1]+1))
    
    for a,b in occurences_counter:
        if a > b:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
            
    print('Binary repr of gamma: ', gamma, 'Binary repr of epsilon:',  epsilon)
    print('Power consumption: ', int(gamma, 2)*int(epsilon, 2))