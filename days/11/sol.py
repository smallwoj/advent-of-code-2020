input = open('input.txt').readlines()
input = [(x.strip()) for x in input]

input = [list(x) for x in input]
input = [x for x in input if x]
import copy

class State:
    def __init__(self, state) -> None:
        self.state = state
    
    def generate_next(self):
        return_state = copy.deepcopy(self.state)
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != '.':
                    count = 0
                    for r in range(-1, 2):
                        for s in range(-1, 2):
                            if 0 <= i + r < len(self.state) and 0 <= j+s < len(self.state[i]) and (s or r):
                                if self.state[i+r][j+s] == '#':
                                    count += 1
                    if count >= 4 and self.state[i][j] == '#':
                        return_state[i][j] = 'L'
                    elif count == 0 and self.state[i][j] == 'L':
                        return_state[i][j] = '#'
        return State(return_state), self.state == return_state

    def generate_next2(self):
        return_state = copy.deepcopy(self.state)
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != '.':
                    count = 0
                    for r in range(-1, 2):
                        for s in range(-1, 2):
                            if not (s or r):
                                continue
                            x = i + r
                            y = j + s
                            found = False
                            while 0 <= x < len(self.state) and 0 <= y < len(self.state[i]) and not found:
                                if self.state[x][y] in '#L':
                                    found = True
                                    if self.state[x][y] == '#':
                                        count += 1
                                else:
                                    x+=r
                                    y+=s
                    if count >= 5 and self.state[i][j] == '#':
                        return_state[i][j] = 'L'
                    elif count == 0 and self.state[i][j] == 'L':
                        return_state[i][j] = '#'
        return State(return_state), self.state == return_state

found = False
state = State(input)
while not found:
    state, found = state.generate_next()
count = 0
for line in state.state:
    for x in line:
        if x == '#':
            count += 1
print(f'Part 1: {count}')

found = False
state = State(input)
while not found:
    state, found = state.generate_next2()
count = 0
for line in state.state:
    for x in line:
        if x == '#':
            count += 1
print(f'Part 2: {count}')
