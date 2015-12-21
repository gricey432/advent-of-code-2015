cache = {}
func_template = '''
def {fname}():
    global cache
    if {fname} not in cache:
        cache["{fname}"] = {body}
    return cache["{fname}"]
'''

commands = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']
with open('7.in') as f:
    for l in f:
        name = "f_" + l.split('->')[1].strip()
        body = ' '.join(
            ["f_" + w + "()" if w not in commands and not w.isdigit() else w for w in l.split('->')[0].strip().split(' ')]
        ).replace('AND', '&').replace('OR', '|').replace('NOT', '~').replace('LSHIFT', '<<').replace('RSHIFT', '>>')
        exec func_template.format(fname=name, body=body)

print f_a()