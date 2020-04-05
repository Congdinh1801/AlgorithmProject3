#dfs_path.py
#Chapter 3 - slide 12 - DFS find path , example: v = dfs_path(graph, 'A', 'D')
def path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

# Sample graph

def dfs_path():
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

    v = path(graph2, 'H', 'P')
    print (v)