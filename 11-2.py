increasing_sequences = [
    ''.join([chr(n), chr(n+1), chr(n+2)])
    for n in range(ord('a'), ord('x') + 1)
]


def increment_string(s):
    bs = [ord(c) for c in s]
    bs[len(bs) - 1] += 1
    for i in range(len(bs) -1, -1, -1):
        if bs[i] > ord('z'):
            bs[i] = ord('a')
            if i > 0:
                bs[i - 1] += 1
        else:
            break
    return ''.join([chr(o) for o in bs])


def has_first(s):
    # can't contain 'i', 'o', 'l'
    return not ('i' in s or 'o' in s or 'l' in s)


def has_second(s):
    # must contain a 3 length increasing sequence
    global increasing_sequences
    for seq in increasing_sequences:
        if seq in s:
            return True
    return False


def has_third(s):
    # must contain 2 pairs of letters 'aa', 'bb'
    i = 0
    found = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            if found:
                return True
            else:
                found += 1
            i += 1
        i += 1
    return False


def is_valid(s):
    return has_first(s) and has_second(s) and has_third(s)


result = 'hxbxwxba'
while True:
    result = increment_string(result)
    if is_valid(result):
        break
# Twice
while True:
    result = increment_string(result)
    if is_valid(result):
        break

print result