input = open('input.txt').readlines()
input = [x.strip() for x in input]

class CubeOfLife:
    def __init__(self, initial_state):
        self.state = initial_state
        # Ensure all the valid cells are generated
        state_copy = initial_state.copy()
        for cell in state_copy:
            self.neighbourhood(cell)

    def neighbourhood(self, cell):
        N = dict()
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0 ,1]:
                    curr = (cell[0] + x, cell[1] + y, cell[2] + z)
                    if curr != cell:
                        if curr not in self.state:
                            self.state[curr] = False
                        N[curr] = self.state[curr]
        return N
    
    def next_cycle(self):
        state_copy = self.state.copy()
        for cell in state_copy:
            self.neighbourhood(cell)
        state_copy = self.state.copy()
        next_state = dict()
        for cell in state_copy:
            N = self.neighbourhood(cell)
            #print(sum(N.values()))
            num = sum(N.values())
            if self.state[cell]:
                if num == 2 or num == 3:
                    next_state[cell] = True
                else:
                    next_state[cell] = False
            else:
                if num == 3:
                    next_state[cell] = True
                else:
                    next_state[cell] = False

        self.state = next_state
        #print(self.count_active())
    
    def count_active(self):
        count = 0
        for cell in self.state:
            if self.state[cell]:
                count += 1
        return count
    
    def display(self, z):
        to_display = dict()
        for cell in self.state:
            if cell[2] == z:
                to_display[(cell[0], cell[1])] = '#' if self.state[cell] else '.'
        x_vals = sorted(set(map(lambda x: x[0], to_display.keys())))
        y_vals = sorted(set(map(lambda x: x[1], to_display.keys())))
        print('z={}'.format(z))
        print('from x in {} and y in {}'.format(x_vals, y_vals))
        for x in x_vals:
            string = ''
            for y in y_vals:
                string += to_display[(x, y)]
            print(string)

# parse input
initial_state = dict()
for x, line in enumerate(input):
    for y, char in enumerate(line):
        initial_state[(x,y,0)] = char == '#'

simulation = CubeOfLife(initial_state)
for _ in range(6):
    simulation.next_cycle()

print(f'Part 1: {simulation.count_active()}')

class HyperCubeOfLife(CubeOfLife): # same idea, different neighbourhood
    def neighbourhood(self, cell):
        N = dict()
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0 ,1]:
                    for w in [-1, 0, 1]:
                        curr = (cell[0] + x, cell[1] + y, cell[2] + z, cell[3] + w)
                        if curr != cell:
                            if curr not in self.state:
                                self.state[curr] = False
                            N[curr] = self.state[curr]
        return N

# parse input
initial_state = dict()
for x, line in enumerate(input):
    for y, char in enumerate(line):
        initial_state[(x,y,0,0)] = char == '#'

simulation = HyperCubeOfLife(initial_state)
for _ in range(6):
    simulation.next_cycle()

print(f'Part 2: {simulation.count_active()}')

