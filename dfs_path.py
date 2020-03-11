#dfs_path.py
#Chapter 3 - slide 12 - DFS find path , example: v = dfs_path(graph, 'A', 'D')
def dfs_path(graph, start, goal):
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
graph1 = {'A': set(['B', 'E']),
         'B': set(['A', 'C']),
         'C': set(['B', 'D', 'E']),
         'D': set(['C']),
         'E': set(['A', 'C'])}

v = dfs_path(graph1, 'A', 'D')
print (v)