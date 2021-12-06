class Line:
    def __init__(self,x1:int,y1:int,x2:int,y2:int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __repr__(self) -> str:
        return "<%s %s> -> <%s %s>" % (self.x1, self.y1, self.x2, self.y2)

# Calcules the point where 2 lines intercept
def line_intersection(source: Line, destiny: Line):
    i1 = source.y2 - source.y1
    j1 = source.x1 - source.x2
    k1 = i1*(source.x1) + j1*(source.y1)
  
    i2 = destiny.y2 - destiny.y1
    j2 = destiny.x1 - destiny.x2
    k2 = i2*(destiny.x1) + j2*(destiny.y1)
  
    determinant = i1*j2 - i2*j1
  
    
    if (determinant == 0):
        # Lines are parallel
        return None
    else:
        x = (j2*k1 - j1*k2)/determinant
        y = (i1*k2 - i2*k1)/determinant
    return (x, y)

intersections = {}
lines = []

with open('AdventOfCode2021/day05/day05.input', 'r+') as f:
    for line in f.readlines():
        source, destiny = line.split(' -> ')
        sx, sy = map(int, source.split(',')); dx, dy = map(int, destiny.split(','))
        lines.append(Line(sx,sy,dx,dy))

print(line_intersection(Line(0,0,0,6), Line(-2,3,2,3)))