#ADJACENCY LIST
class Solution:
    def printGraph(v,edges):
        adj = []
        for i in range(v):
            adj.append([])
        for n,m in edges:
            adj[n].append(m)
            adj[m].append(n)
        for lst in adj:
            lst.sort()
        return adj
