import string

processed = []
graph = {
    'start': {},
    'a': {},
    'b': {},
    'final': {}
}
costs = {
    'a': 6,
    'b': 2,
    'final': float("inf")
}
parents = {
    'a': 'start',
    'b': 'start',
    'final': None
}

graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a']['final'] = 1
graph['b']['a'] = 3
graph['b']['final'] = 5


def find_lowest_code(costs: dict) -> string:
    lowest = float('inf')
    lowest_node = None
    for node in costs:
        if costs[node] < lowest and node not in processed:
            lowest = costs[node]
            lowest_node = node
    return lowest_node


def dijkstra():
    node = find_lowest_code(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_code(costs)
