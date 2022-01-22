#Personal implementation of Dijkstra's algorithm 

import math 

g1 = [[0, 3, 1, 2, 0, 0],
     [3, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 4, 2],
     [2, 0, 0, 0, 1, 0],
     [0, 0, 4, 1, 0, 0],
     [0, 0, 2, 0, 0, 0]]

g2 =[[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

def dijkstra(g, start, v):
    
    s = [start]
    t = [float('inf') if i != start else 0 for i in range(v)]
    
    #w <- s[0], g[s[0]] <- neighborhood
    while len(s) != v:
        for i in range(v):  #i <- v (neighbor of w)
            if i not in s and g[s[0]][i] != 0:
                t[i] = min(t[i], t[s[0]] + g[s[0]][i])  #min{t(v), t(w) + weight(vw)}
        w = t.index(max(t))
        for i in range(v):
            if i not in s and t[i] < t[w]:
                w = i
        s.insert(0, w)
        
    print("Vertex   Distance from source")
    for i in range(v):
        print(f"{i}                 {t[i]}")
        
dijkstra(g2, 0, len(g2))