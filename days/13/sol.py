input = open('input.txt').readlines()
input = [x.strip() for x in input]

class Bus:
    def __init__(self, id):
        self.id = id
    def next(self, time):
        num = self.id
        while num < time:
            num += self.id
        return num
    def __str__(self):
        return str(self.id)

def find_bus(buses: list, time: int):
    buses = [x for x in buses if x != 'x']
    bus = min(buses, key=lambda x: x.next(time))
    return bus.id * (bus.next(time) - time)

def find_buses(buses):
    '''
    shoutout to this reddit post cause i dont know about a number theorem :(
        https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfo4b1z/?utm_source=reddit&utm_medium=web2x&context=3
    '''
    buses = [tup for tup in enumerate(buses) if tup[1] != 'x']
    jump = buses[0][1].id
    start = 0
    for i,b in buses[1:]:
        if b != 'x':
            while (start + i) % b.id != 0:
                start += jump
            jump *= b.id
    return start

time = int(input[0])
buses = []
for id in input[1].split(','):
    if id == 'x':
        buses.append('x')
    else:
        buses.append(Bus(int(id)))

print(f'Part 1: {find_bus(buses, time)}')
print(f'Part 2: {find_buses(buses)}')
