input = open('input.txt').readlines()
input = [x.strip() for x in input]

def reduce(input: str, bottom: int, top: int) -> int:
    for c in input[:-1]:
        if c in 'FL':
            top = (top + bottom) // 2
        elif c in 'BR':
            bottom = (top + bottom) // 2 + 1
    val = min(top, bottom) if input[-1] in 'FL' else max(top, bottom)
    return val

def get_seat_id(boarding_pass: str) -> int:
    return 8*reduce(boarding_pass[:7], 0, 127) + reduce(boarding_pass[7:], 0, 7)

seat_ids = list(map(get_seat_id, input))
p1 = max(seat_ids)
print(f'Part 1: {p1}')

import itertools
# prolly really inefficient but thats Okay
def get_possible_passes():
    total_rows = [''.join(x) for x in itertools.product('FB', repeat=7)]
    total_cols = [''.join(x) for x in itertools.product('RL', repeat=3)]
    possible = set()
    for row in total_rows:
        for col in total_cols:
            possible.add(row + col)
    return possible

p2 = -1
for boarding_pass in get_possible_passes() - set(input):
    id = get_seat_id(boarding_pass)
    if id not in seat_ids and all([id + x in seat_ids for x in [-1, 1]]):
        p2 = id

print(f'Part 2: {p2}')
