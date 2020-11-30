input = open('input.txt').readlines()
input = [x.strip() for x in input]

def count_trees(terrain, start, slope):
    pos = start
    count = 0
    while pos[1] < len(terrain):
        if terrain[pos[1]][pos[0]%len(terrain[pos[1]])] == '#':
            count+=1
        pos = (pos[0]+slope[0], pos[1]+slope[1])
    return count

start = (0,0)
slope = (3,1)
count = count_trees(input, start, slope)
print(f'Part 1: {count}')

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
counts = [count_trees(input, start, s) for s in slopes]
prod = 1
for c in counts:
    prod*=c

print(f'Part 2: {prod}')
