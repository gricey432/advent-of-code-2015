commands = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']

# Build up instruction list
instructions = []
with open('7.in') as _f:
    for _l in _f:
        instructions.append({
            'orig': _l,
            'dest': "var_" + _l.split('->')[1].strip(),
            'prereqs': ["var_" + _w for _w in _l.split('->')[0].strip().split(' ') if _w not in commands and not _w.isdigit()],
            'eval': ' '.join(["var_" + _w if _w not in commands and not _w.isdigit() else _w for _w in _l.split('->')[0].strip().split(' ')]).replace('AND', '&').replace('OR', '|').replace('NOT', '~').replace('LSHIFT', '<<').replace('RSHIFT', '>>'),
            'needs_sort': True
        })

# Sort so dependencies come first
def run_sort(instructions):
    moved = 0
    for i in range(len(instructions) - 1, -1, -1):
        base = instructions[i]
        if base['needs_sort']:
            for prereq in base['prereqs']:
                for j in range(i, len(instructions)):
                    comp = instructions[j]
                    if comp['dest'] == prereq:
                        moving = instructions.pop(j)
                        moving['needs_sort'] = True
                        instructions.insert(i, moving)
                        moved += 1
            base['needs_sort'] = False
    return moved > 0

while run_sort(instructions):
    pass

for instruction in instructions:
    exec ("{} = {}".format(
        instruction['dest'],
        instruction['eval']
    ))

print var_a