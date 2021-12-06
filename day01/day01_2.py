class Queue3:
    def __init__(self) -> None:
        self.queue = []   
    def add(self, value) -> None:
        if len(self.queue) < 3:
            self.queue.append(int(value))
            return
        self.queue = self.queue[1:]
        self.queue.append(int(value))
    def sum(self):
        if len(self.queue) < 3:
            return -1
        return sum(self.queue)
    
previous_value = 0
counter = -1
q = Queue3()

with open('AdventOfCode2021/day01/day01.input', 'r+') as f:
    for line in f.readlines():
        q.add(line)
        if q.sum() > previous_value:
            counter+=1
        previous_value = q.sum()
print('Times the depth increased: ', counter)