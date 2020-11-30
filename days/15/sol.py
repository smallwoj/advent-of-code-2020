# TODO: get input from file

mem = dict()
spoken = []

def add(num, turn):
    if num in mem:
        to_ret = turn - mem[num]['last']
        mem[num]['last'] = turn
    else:
        mem[num] = {
            'last': turn,
            'num': len(mem) + 1,
        }
        to_ret = 0
    print(turn, num, to_ret)
    return to_ret

next = input[0]
for i, num in enumerate(input):
    add(num, i + 1)
    spoken.append(num)

turn = len(input)
next = input[-1]
while len(spoken) != 30000000:
    next = add(next, turn)
    spoken.append(next)
    turn += 1

print(f'Part 1: {spoken[2019]}')
print(f'Part 2: {spoken[-1]}')
