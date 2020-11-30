input = open('input.txt').readlines()
input = [x.strip() for x in input]

rules = dict()
# organize input
for line in input:
    curr_colour = line.split('bags')[0].strip()
    rules[curr_colour] = []
    bags = line.split('contain')[1].split(',')
    for bag in bags:
        bag = bag.strip().split(' ')
        num = bag[0]
        if num != 'no':
            bag = ' '.join(bag[1:-1])
            # unfortunately i didnt account for the multiple bag coutns, leading to this kinda smelly list of dicts.
            # This could easily be just a dict of dicts
            rules[curr_colour].append({bag: int(num)})


def search_bag(curr_bag, bags):
    if bags[curr_bag]:
        if 'shiny gold' in map(lambda x: list(x.keys())[0], bags[curr_bag]):
            return True
        else:
            for bag in bags[curr_bag]:
                if search_bag(list(bag.keys())[0], bags):
                    return True
    return False
count = 0
for bag in rules.keys():
    if search_bag(bag, rules):
        count += 1
print(f'Part 1: {count}')

def count_bags(curr_bag, bags): # i spent so long passing the current count just to not need it
    if bags[curr_bag]:
        curr_count = 0
        for bag in bags[curr_bag]:
            bag_name = list(bag.keys())[0]
            for i in range(bag[bag_name]):
                curr_count += 1
                curr_count += count_bags(bag_name, bags)
        return curr_count
    return 0

print(f'Part 2: {count_bags("shiny gold", rules)}')
