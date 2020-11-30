rules, input = open('input.txt').read().split('\n\n')
rules = rules.split('\n')
input = input.split('\n')
def build_rules(rules):
    rule_dict = dict()
    for rule in rules:
        num, rule = rule.split(': ')
        num = int(num)
        if '"' in rule:
            rule_dict[num] = rule.split('"')[1]
        else:
            rule_dict[num] = set()
            for subrule in rule.split('|'):
                subrule = subrule.strip()
                subrule = [int(x) for x in subrule.split(' ')]
                rule_dict[num].add(tuple(subrule))
    return rule_dict
rules = build_rules(rules)

# This was what i thought up for part 1, its a recursive lookup function, keeping track of what has been matched so far
def validate(string, start):
    if not string:
        return True, string
    rule = rules[start]
    if type(rule) == str:
        if rule == string[0]:
            return True, string[0]
        else:
            return False, None
    else:
        valid = False
        match = None
        for subrule in rule:
            matched = ''
            test = string
            is_valid = False
            for subsubrule in subrule:
                is_valid, match = validate(test[len(matched):], subsubrule)
                if is_valid:
                    matched += match
                else:
                    break
            if is_valid:
                valid = True
                match = matched
                break
        return valid, match

s = 0
for string in input:
    valid, match = validate(string, 0)
    if valid and match == string:
        s += 1
print(f'Part 1: {s}')

# This is what i did for part 2, can work for part 1 too
# It keeps track of the recursion depth, where the max depth is set based on the length of the string being tested
# With the loops in the rules, it can only loop a maximum of MAX_DEPTH times
MAX_DEPTH = 100
def build_regex(rule, depth):
    rule = rules[rule]
    if type(rule) == str:
        return rule
    elif depth >= MAX_DEPTH:
        return ''
    else:
        res = '('
        res += '|'.join([''.join([build_regex(r, depth + 1) for r in rs]) for rs in rule])
        res += ')'
        return res

new_rules = '''8: 42 | 42 8
11: 42 31 | 42 11 31'''.split('\n')
new_rules = build_rules(new_rules)
for rule in new_rules:
    rules[rule] = new_rules[rule]

import re
s = 0
for line in input:
    MAX_DEPTH = len(line)
    regex = f'^{build_regex(0, 0)}$'
    if re.match(regex, line):
        s+=1
print(f'Part 2: {s}')
