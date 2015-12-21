with open('9.in') as f:
    connections = [{
        'start': ls[0],
        'end': ls[2],
        'distance': int(ls[4])
    } for ls in [l.strip().split(' ') for l in f]]

all_cities = set(c['start'] for c in connections)

def min_path(cities, connections, all_cities):
    current_city = cities[len(cities) - 1]
    current_connections = [c for c in connections if c['start'] == current_city and c['end'] not in cities]
    if len(current_connections) is 0:
        if len(cities) == len(all_cities):
            return 0
        return
    distances = []
    for connection in current_connections:
        new_cities = cities + [connection['end']]
        result = min_path(new_cities, connections, all_cities)
        if result is not None:
            distances.append(result + connection['distance'])
    if len(distances) is 0:
        return None
    return min(distances)

print min([r for r in [min_path([start], connections, all_cities) for start in all_cities] if r is not None])
for start in all_cities:
    print start, min_path([start], connections, all_cities)