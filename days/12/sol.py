input = open('input.txt').readlines()
input = [x.strip() for x in input]

def travel(start, input):
    dir = 0
    curr = start
    for command in input:
        code, num = command[0], int(command[1:])
        if code == 'L':
            dir = (dir+num)%360
        elif code == 'R':
            dir -= num
            if dir < 0:
                dir = 360 + dir
            dir %= 360
        elif code == 'F':
            if dir // 90 == 0:
                code = 'E'
            elif dir // 90 == 1:
                code = 'N'
            elif dir // 90 == 2:
                code = 'W'
            else:
                code = 'S'
        if code == 'N':
            curr = (curr[0], curr[1] + num)
        elif code == 'E':
            curr = (curr[0] + num, curr[1])
        elif code == 'S':
            curr = (curr[0], curr[1] - num)
        elif code == 'W':
            curr = (curr[0] - num, curr[1])
    return curr

def travel2(start, waypoint_start, input):
    curr = start
    waypoint = waypoint_start
    for command in input:
        code, num = command[0], int(command[1:])
        if code == 'R':
            num = 360-num
        if code in 'RL':
            if num == 90:
                waypoint = (-waypoint[1], waypoint[0])
            elif num == 180:
                waypoint = (-waypoint[0], -waypoint[1])
            elif num == 270:
                waypoint = (waypoint[1], -waypoint[0])
                
        if code == 'F':
            for _ in range(num):
                curr = (curr[0] + waypoint[0], curr[1] + waypoint[1])
        if code == 'N':
            waypoint = (waypoint[0], waypoint[1] + num)
        elif code == 'E':
            waypoint = (waypoint[0] + num, waypoint[1])
        elif code == 'S':
            waypoint = (waypoint[0], waypoint[1] - num)
        elif code == 'W':
            waypoint = (waypoint[0] - num, waypoint[1])
    return curr


p1 = travel((0,0), input)
p1 = sum(map(abs, p1))
print(f'Part 1: {p1}')
p2 = travel2((0,0), (10,1), input)
p2 = sum(map(abs, p2))
print(f'Part 2: {p2}')
