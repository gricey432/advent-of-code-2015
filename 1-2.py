with open('1.in') as f:
    l = f.readline()
    c = 1
    while True:
        if eval("0" + l[0:c].replace('(', '+1').replace(')', '-1')) < 0:
            break
        c += 1
print c