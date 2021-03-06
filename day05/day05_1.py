intersections = {}
intersection_counter = 0

with open('AdventOfCode2021/day05/day05.input', 'r+') as f:
    for line in f.readlines():
        source, destiny = line.split(' -> ')
        sx, sy = map(int, source.split(',')); dx, dy = map(int, destiny.split(','))

        if sx == dx:
            if sy > dy:
                for i in range(0,sy-dy+1):
                    if (sx, dy+i) in intersections:
                        intersections[(sx, dy+i)] += 1
                    else:
                        intersections[(sx, dy+i)] = 1
            else:
                for i in range(0,dy-sy+1):
                    if (sx, sy+i) in intersections:
                        intersections[(sx, sy+i)] += 1
                    else:
                        intersections[(sx, sy+i)] = 1
                
        if sy == dy:
            if sx > dx:
                for i in range(0,sx-dx+1):
                    if (dx+i, sy) in intersections:
                        intersections[(dx+i, sy)] += 1
                    else:
                        intersections[(dx+i, sy)] = 1
            else:
                for i in range(0,dx-sx+1):
                    if (sx+i, sy) in intersections:
                        intersections[(sx+i, sy)] += 1
                    else:
                        intersections[(sx+i, sy)] = 1

    for k in intersections:
        if intersections[k] > 1:
            intersection_counter+=1
    
print(intersection_counter)
    