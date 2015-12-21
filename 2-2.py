import itertools, operator

total = 0
for line in open('2.in'):
    dim = [int(n) for n in line.split('x')]
    perimeters = [2 * (a + b) for a, b in itertools.combinations(dim, 2)]
    volume = reduce(operator.mul, dim, 1)
    total += min(perimeters) + volume

print total