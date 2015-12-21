    cache = {}
    func_template = '''
    def {fname}():
        global cache
        if "{fname}" not in cache:
            cache["{fname}"] = {body}
        return cache["{fname}"]
    '''

    with open('7.in') as f:
        for line in f:
            name = "f_" + line.split('->')[1].strip()
            body = ' '.join(
                [
                    "f_" + wire + "()" if wire not in ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT'] and not wire.isdigit()
                    else wire
                    for wire in line.split('->')[0].strip().split(' ')
                ]
            ).replace('AND', '&')\
            .replace('OR', '|')\
            .replace('NOT', '~')\
            .replace('LSHIFT', '<<')\
            .replace('RSHIFT', '>>')
            exec func_template.format(fname=name, body=body)

    print f_a()