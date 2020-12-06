input = open('input.txt').read()
input = input.split('\n\n')



def process_batches(input):
    any_count = 0
    all_count = 0
    for batch in input:
        answered = []
        batch = batch.split('\n')
        for person in batch:
            answers = set()
            for answer in person:
                answers.add(answer)
            answered.append(answers)
        any_answered = answered[0].union(*answered[1:])
        any_count += len(any_answered)
        all_answered = answered[0].intersection(*answered[1:])
        all_count += len(all_answered)
    return any_count, all_count


p1, p2 = process_batches(input)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
