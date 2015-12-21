addresses = set()
x, y = 0, 0
with open('3.in') as f:
    for line in f:
        for c in line:
            addresses.add(str(x) + '_' + str(y))
            if c is '^':
                y -= 1
            elif c is 'v':
                y += 1
            elif c is '<':
                x -= 1
            elif c is '>':
                x += 1
print len(addresses)