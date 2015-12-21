import re

code_count = 0
recode_count = 0

with open('8.in') as f:
    for line in f:
        code_count += len(line.strip())
        recode_count += len(re.escape(line.strip())) + 2
print recode_count - code_count