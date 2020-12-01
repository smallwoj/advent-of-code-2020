input = open('input.txt').readlines()

input = [int(x.strip()) for x in input]

def get_product(input: list):
    for x in input:
        for y in input:
            if x != y:
                if x + y == 2020:
                    return x * y
    return -1

print(get_product(input))
