addresses = set()
x_1, y_1 = x_2, y_2 = 0, 0
robo = False
with open('3.in') as f:
    for line in f:
        for c in line:
            if robo:
                addresses.add(str(x_1) + '_' + str(y_1))
                if c is '^':
                    y_1 -= 1
                elif c is 'v':
                    y_1 += 1
                elif c is '<':
                    x_1 -= 1
                elif c is '>':
                    x_1 += 1
            else:
                addresses.add(str(x_2) + '_' + str(y_2))
                if c is '^':
                    y_2 -= 1
                elif c is 'v':
                    y_2 += 1
                elif c is '<':
                    x_2 -= 1
                elif c is '>':
                    x_2 += 1
            robo = not robo
print len(addresses)