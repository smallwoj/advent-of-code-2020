input = open('input.txt').read()
input = input.split('\n\n')

import re
# organize into python dictionaries
def parse_passports(input):
    passports = []
    for batch in input:
        fields = dict()
        str_fields = re.split(r'[\n ]', batch)
        for field in str_fields:
            key, val = field.split(':')
            fields[key] = val
        passports.append(fields)
    return passports

def count_valid(passports, required, optional): # thought optional was going to play a bigger role lol
    count_valid = 0
    count_valid_and_present = 0
    for passport in passports:
        present = False
        if all([req in passport.keys() for req in required.keys()]):
            count_valid += 1
            present = True
        if present:
            valid = True
            for field in required.keys():
                if not required[field](passport[field]):
                    valid = False
            if valid:
                count_valid_and_present += 1 
    return count_valid, count_valid_and_present

passports = parse_passports(input)
# inspired by the vuetify validation rules system, list the fields and their rules
required = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002, 
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020, 
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030, 
    'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76), 
    'hcl': lambda x: re.match(r'#[0-9a-f]{6}', x), 
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
    'pid': lambda x: len(x) == 9 and x.isnumeric(),
}
optional = ['cid']
p1, p2 = count_valid(passports, required, optional)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
