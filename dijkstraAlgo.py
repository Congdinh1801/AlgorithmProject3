# Python implementation of Dijkstra's algorithm
#https://gist.github.com/kachayev/5990802

from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

def dijk():
    edges = [
        ("A", "B", 22), 
        ("A", "C" ,9), 
        ("A", "D" ,12), 
        ("B", "H", 34),
        ("B", "C", 35), 
        ("B", "F", 36), 
        ("C", "D", 4), 
        ("C", "F", 42), 
        ("C", "E", 65), 
        ("D", "E", 33), 
        ("D", "I", 30), 
        ("E", "F", 18), 
        ("E", "G", 23), 
        ("F", "H", 24), 
        ("F", "G", 39), 
        ("G", "H", 25), 
        ("G", "I", 21), 
        ("H", "I", 19)
 
    ]

    print ("=== Dijkstra ===")
    #print (edges)
    print ("A -> F:")
    output = dijkstra(edges, "A", "F")
    print (output)

    print ("A -> I:")
    output1 = dijkstra(edges, "A", "I")
    print(output1)

    print("A -> E")
    output2 = dijkstra(edges, "A", "E")
    print(output2)

    print("A -> H")
    output3 = dijkstra(edges, "A", "H")
    print(output3)

