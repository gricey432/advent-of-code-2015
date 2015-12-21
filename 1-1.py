with open('1-1.in') as f:
    l = f.readline()
    print eval("0" + l.replace('(', '+1').replace(')', '-1'))