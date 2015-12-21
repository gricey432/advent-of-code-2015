import itertools

total = 0
for line in open('2.in'):
    dim = [int(n) for n in line.split('x')]
    sides = [a * b for a, b in itertools.combinations(dim, 2)]
    total += sum(sides) * 2 + min(sides)

print total