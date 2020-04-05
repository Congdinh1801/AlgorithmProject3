#bfs traverse graph
def bfsTrav(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

#bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}
def bfs():
    
    graph2 = {'A': set(['B', 'E', 'F']),
         'B': set(['A', 'C', 'F']),
         'C': set(['B', 'D', 'G']),
         'D': set(['C','G']),
         'E': set(['A', 'F','I']),
         'F': set(['A', 'B', 'E', 'I']),
         'G': set(['C', 'D', 'J']),
         'H': set(['K', 'L']),
         'I': set(['E', 'F', 'J', 'M']),
         'J': set(['G', 'I']),
         'K': set(['H', 'L', 'O']),
         'L': set(['H', 'K', 'P']),
         'M': set(['I', 'N']),
         'N': set(['M']),
         'O': set(['K']),
         'P': set(['L'])}

    v = bfsTrav(graph2, 'A')
    print("Starting from A: ")
    print(v)
    v = bfsTrav(graph2, 'H')
    print("Starting from H: ")
    print(v)

