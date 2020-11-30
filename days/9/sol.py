input = open('input.txt').readlines()
input = [int(x.strip()) for x in input]



curr = 25
found = False
while curr < len(input) and not found:
    num = input[curr]
    preamble = input[curr-25:curr]
    curr_found = False
    for x in preamble:
        for y in preamble:
            if x != y:
                if x + y == input[curr]:
                    curr_found = True
    if not curr_found:
        found = num
    curr += 1
print(f'Part 1: {found}')

range_val = []
for i in range(len(input)): # Theres prolly a faster way to do this
    for j in range(i+1, len(input)):
        if sum(input[i:j+1]) == found:
            range_val = [i, j]
found = input[range_val[0]:range_val[1]+1]
print(f'Part 2: {min(found) + max(found)}')