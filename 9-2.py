with open('9.in') as f:
    connections = []
    for l in f:
        ls = l.strip().split(' ')
        connections.append({
            'start': ls[0],
            'end': ls[2],
            'distance': int(ls[4])
        })
        connections.append({
            'end': ls[0],
            'start': ls[2],
            'distance': int(ls[4])
        })

all_cities = set(c['start'] for c in connections)

def max_path(cities, connections, all_cities):
    current_city = cities[len(cities) - 1]
    current_connections = [c for c in connections if c['start'] == current_city and c['end'] not in cities]
    if len(current_connections) is 0:
        if len(cities) == len(all_cities):
            return 0
        return
    distances = []
    for connection in current_connections:
        new_cities = cities + [connection['end']]
        result = max_path(new_cities, connections, all_cities)
        if result is not None:
            distances.append(result + connection['distance'])
    if len(distances) is 0:
        return None
    return max(distances)

print max([r for r in [max_path([start], connections, all_cities) for start in all_cities] if r is not None])
