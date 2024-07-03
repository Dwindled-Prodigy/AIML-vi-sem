graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        M = queue.pop(0)
        print(M)

        for neighbor in graph[M]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs(visited, graph, '5')