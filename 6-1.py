import re

prog = re.compile("(.+) (\d+),(\d+) through (\d+),(\d+)")

lights = [[False for col in range(1000)] for row in range(1000)]
for l in open('6.in'):
    matches = prog.match(l)
    method, x_1, y_1, x_2, y_2 = matches.groups()
    x_1, y_1, x_2, y_2 = int(x_1), int(y_1), int(x_2), int(y_2)
    for x in range(x_1, x_2 + 1):
        for y in range(y_1, y_2 + 1):
            if method == "turn on":
                lights[x][y] = True
            elif method == "turn off":
                lights[x][y] = False
            else:
                lights[x][y] = not lights[x][y]

print sum([sum([1 for y in x if y]) for x in lights])