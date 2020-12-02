input = open('input.txt').readlines()
input = [x.strip() for x in input]

valid1 = 0
valid2 = 0
for line in input:
    constraint, password = [x.strip() for x in line.split(':')]
    count_range, value = constraint.split(' ')
    min, max = [int(x) for x in count_range.split('-')]
    # part 1 specific
    if password.count(value) in range(min, max+1):
        valid1 += 1
    # part 2 specific
    pos1Valid = password[min-1] == value
    pos2Valid = password[max-1] == value
    if pos1Valid ^ pos2Valid: # xor is the name of the game
        valid2 += 1  

print(f'part 1: {valid1}')
print(f'part 2: {valid2}')
