input = open('input.txt').readlines()

input = [int(x.strip()) for x in input]

def get_product(input: list):
    seen_combs = set()
    for x in input:
        for y in input:
            for z in input:
                if frozenset((x,y,z)) not in seen_combs and not(x == y == z):
                    if x + y + z == 2020:
                        return x * y * z
                    seen_combs.add(frozenset((x,y,z)))
    return -1

print(get_product(input))
