import collections
from string import ascii_lowercase

def is_good(w):
    if 'ab' in w or 'cd' in w or 'pq' in w or 'xy' in w:
        return False
    ls = collections.Counter(w)
    if sum([ls.get(l, 0) for l in ['a', 'e', 'i', 'o', 'u']]) < 3:
        return False
    for c in ascii_lowercase:
        if c + c in w:
            return True
    return False

print len([w for w in open('5.in') if is_good(w)])