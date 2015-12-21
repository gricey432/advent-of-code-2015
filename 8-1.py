code_count = 0
memory_count = 0

with open('8.in') as f:
    for line in f:
        code_count += len(line.strip())
        exec "memory_count += len({})".format(line.strip())
print code_count - memory_count