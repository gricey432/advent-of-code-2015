import collections

def has_first(w):
    for i in range(len(w) - 2):
        if w[i] == w[i + 2]:
            return True
    return False

def has_second(w):
    pairs_even = [w[n:n+2] for n in range(0, len(w) - 1, 2)]
    pairs_odd = [w[n:n+2] for n in range(1, len(w), 2)]
    for pair in pairs_even:
        if pairs_even.count(pair) > 1:
            return True
    for pair in pairs_odd:
        if pairs_odd.count(pair) > 1:
            return True
    for i in range(len(pairs_even)):
        for j in range(len(pairs_odd)):
            if pairs_even[i] == pairs_odd[j] and i != j and i != j + 1:
                return True
    return False

print len([w for w in open('5.in') if has_first(w) and has_second(w)])