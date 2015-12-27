import json


def recursive_sum(obj):
    if type(obj) is int:
        return obj
    elif type(obj) is unicode:
        return 0
    elif type(obj) is list:
        return sum(recursive_sum(o) for o in obj)
    elif type(obj) is dict:
        return sum(recursive_sum(o) for o in obj.values())
    else:
        raise


with open('12.in') as f:
    data = json.load(f)

print recursive_sum(data)