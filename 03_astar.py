def h(n):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }

    return H_dist[n]


graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

def get_neighbours(v):
    if v in graph_nodes:
        return graph_nodes[v] 
    else:
        return None 


def astarAlgo(startnode , stopnode):
    open_set = set(startnode)
    closed_set = set()
    g = {}
    parents = {}
    g[startnode] = 0 
    parents[startnode] = startnode

    while open_set:
        n = None 

        for v in open_set:
            if n == None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n == stopnode or graph_nodes[n] == None :
            pass 
        else:
            for (m ,weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set :
                    open_set.add(m)
                    parents[m] = n 
                    g[m] = g[n] + weight 

                else:
                    if g[m] > g[n] + weight :
                        g[m] = g[n] + weight 
                        parents[m] = n 

                        if m in closed_set :
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None :
            print('The path doesnt exist')
            return None 

        if n == stopnode :
            path = [] 

            while parents[n] != n:
                path.append(n)
                n = parents[n] 

            path.append(startnode)
            path.reverse()
            print(path)
            return path 

        open_set.remove(n)
        closed_set.add(n)

    print('Path doesnt exist')
    return None 


astarAlgo('A' , 'J')