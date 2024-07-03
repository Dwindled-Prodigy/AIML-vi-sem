# graph = {
#     '5': ['3', '7'],
#     '3': ['2', '4'],
#     '7': ['8'],
#     '2': [],
#     '4': ['8'],
#     '8': []
# }

graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)


dfs(visited, graph, '1')