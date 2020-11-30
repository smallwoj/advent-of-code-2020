input = open('input.txt').read()
info, ticket, nearby = input.split('\n\n')

def build_info(info):
    new_info = dict()
    for line in info.split('\n'):
        attr, rules = line.split(':')
        attr = attr.strip()
        rules = rules.strip()
        new_info[attr] = []
        for str_range in rules.split('or'):
            str_range = str_range.strip()
            minimum, maximum = map(int, str_range.split('-'))
            new_info[attr].append({'min': minimum, 'max': maximum})
    return new_info

info = build_info(info)
ticket = [int(x) for x in ticket.split('\n')[1].split(',')]
nearby = [list(map(int, x.split(','))) for x in nearby.split('\n')[1:]]
def get_invalid(info, nearby):
    invalid = []
    for ticket in nearby:
        for num in ticket:
            valid = []
            for attr in info:
                valid.extend([rule['min'] <= num <= rule['max'] for rule in info[attr]])
            if not any(valid):
                invalid.append(ticket)
    return invalid
invalid = get_invalid(info, nearby)
print(f'Part 1: {len(invalid)}')

valid_nearby = [x for x in nearby if x not in invalid]

possible = [set(info.keys()) for _ in range(len(ticket))]

for tick in valid_nearby:
    for i, num in enumerate(tick):
        if type(possible[i]) == str: continue
        to_remove = set()
        for attr in possible[i]:
            if not any([rule['min'] <= num <= rule['max'] for rule in info[attr]]):
                to_remove.add(attr)
        possible[i] = possible[i] - to_remove

        # Ensuring this worked was the toughest part, propagate it
        while any([len(x) == 1 for x in possible]):
            for j in range(len(possible)):
                if len(possible[j]) == 1 and type(possible[j]) != str:
                    possible[j] = possible[j].pop()
                    for other in possible:
                        if other != possible[j] and type(other) != str:
                            other.remove(possible[j])
prod = 1
for i, col in enumerate(possible):
    if 'departure' in col:
        prod *= ticket[i]
print(f'Part 2: {prod}')
