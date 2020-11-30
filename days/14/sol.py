input = open('input.txt').readlines()
input = [(x.strip()) for x in input]

import re
mask = ''
mem = dict()
for command in input:
    op = command.split(' ')[0]
    if 'mask' in op:
        mask = command.split(' ')[-1]
    else:
        addr = int(re.split(r'[\[\]]', command)[1])
        value = bin(int(command.split(' ')[-1]))
        
        value = str(value).split('b')[1].zfill(len(mask))
        new_value = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                new_value += value[i]
            else:
                new_value += mask[i]
        new_value = sum([2**i for i, bit in enumerate(reversed(new_value)) if int(bit)])
        mem[addr] = new_value

p1 = sum(mem.values())
print(f'Part 1: {p1}')

mem = dict()
        
for command in input:
    op = command.split(' ')[0]
    if 'mask' in op:
        mask = command.split(' ')[-1]
    else:
        value = int(command.split(' ')[-1])
        addr = bin(int(re.split(r'[\[\]]', command)[1]))
        
        addr = str(addr).split('b')[1].zfill(len(mask))
        new_mask = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                new_mask += 'X'
            elif mask[i] == '1':
                new_mask += '1'
            elif mask[i] == '0':
                new_mask += addr[i]
        
        addrs = ['']
        for x in new_mask:
            if x in '10':
                for i in range(len(addrs)):
                    addrs[i] += x
            else: # X
                new_addrs = []
                for i in range(len(addrs)):
                    new_addrs.append(addrs[i] + '1')
                    new_addrs.append(addrs[i] + '0')
                addrs = new_addrs
        addrs = [sum([2**i for i, bit in enumerate(reversed(a)) if int(bit)]) for a in addrs]
        for a in addrs:
            mem[a] = value

p2 = sum(mem.values())
print(f'Part 2: {p2}')
