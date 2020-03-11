#dfs_digraph_traverse.py 
#Chapter 3 - slide 14 - DFS digraph traversal 
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# An iterative DFS implementation 
# 
# -GRAPH: a dictionary of vertex and sdjancent list
# -START: starting vertex for traversal
# -VISITED: a set of visited vertices 
#
def _dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        #print('The stack is:', stack)
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# Sample graph
graph = {'A': set(['B', 'C', 'F']),
         'B': set(['E']),
         'C': set(['D']),
         'D': set(['A', 'H']),
         'E': set(['F', 'G', 'H']),
         'F': set(['B', 'G']),
         'G': set(),
         'H': set(['G'])}


v = _dfs(graph, 'A')
print(v)



# Sample graph
graph1 = {'A': set(['B', 'E']),
         'B': set(['A', 'C']),
         'C': set(['B', 'D', 'E']),
         'D': set(['C']),
         'E': set(['A', 'C'])}

t = 0
v = _dfs(graph1, 'D')
print(v)