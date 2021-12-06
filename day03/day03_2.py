a,b=[],[]
t = (0,0)

with open('AdventOfCode2021/day03/day03.input', 'r+') as f:
    main = list(map(str.strip, f.readlines()))
    main_co2 = main
    for i in range(0, len(main[0])):
        if len(main) > 1:
            for line in main:
                if line[i] == '1':
                    a.append(line)
                else:
                    b.append(line)
            main = a if len(a) >= len(b) else b
            a,b=[],[]
        if len(main_co2) > 1:
            for line in main_co2:
                if line[i] == '1':
                    a.append(line)
                else:
                    b.append(line)
            main_co2 = a if len(a) < len(b) else b
            a,b=[],[]
    print('bin o2:', main[0], '\nbin co2:', main_co2[0])
    print('Life support rating is: ',int(main[0],2),'*',int(main_co2[0],2),'=',int(main_co2[0],2)*int(main[0],2))