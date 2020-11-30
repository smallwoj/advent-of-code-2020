input = open('input.txt').readlines()
input = [x.strip() for x in input]

seen = set()
ptr = 0
acc = 0
while True:
    #print(ptr, acc, input[ptr])
    if ptr in seen:
        break # i know ive violated every single programming convention im sorry i wanted to do it quicc
    seen.add(ptr)
    op, val = input[ptr].split(' ')
    if op == 'acc':
        acc += int(val)
        ptr += 1
    elif op == 'jmp':
        ptr += int(val)
    else: ptr += 1

print(f'Part 1: {acc}')
for i in range(len(input)):
    if 'acc' in input[i]: continue # 😭
    input2 = input.copy()
    op, val = input[i].split(' ')
    if op == 'jmp':
        op = 'nop'
    else:
        op = 'jmp'
    input2[i] = f'{op} {val}'
    seen = set()
    ptr = 0
    acc = 0
    while True:
        if ptr in seen or ptr >= len(input2):
            break # 1️⃣
        seen.add(ptr)
        op, val = input2[ptr].split(' ')
        if op == 'acc':
            acc += int(val)
            ptr += 1
        elif op == 'jmp':
            ptr += int(val)
        else: ptr += 1
    if ptr >= len(input):
        break # 2️⃣ if yall ever catch me code like this give me a slappy
print(f'Part 2: {acc}')

