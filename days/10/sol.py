file_input = open('input.txt').readlines()
file_input = [int(x.strip()) for x in file_input]

def differences(input):
    input = set(input)
    device = max(input) + 3
    input.add(device)
    count = {
        1: 0,
        2: 0,
        3: 0,
    }
    prev = 0
    while input:
        rating = min(input)
        count[rating - prev] += 1
        input.remove(rating)
        prev = rating
    
    return count

count = differences(file_input)
print(f'Part 1: {count[1]*count[3]}')

queue = [0]

count = 1
device = max(file_input) + 3
file_input.append(device)
file_input.append(0)
file_input.sort()
seen = set()
queue = [0]
cache = dict()
for x in file_input:
    cache[x] = 0
cache[0] = 1
# i completely misunderstood this question : ( so i did this a lot slower this time
# i also forgot dynamic programming existed
for x in file_input:
    for step in range(1,4):
        if x + step in cache:
            cache[x+step] += cache[x]
print(f'Part 2: {cache[max(cache)]}')

