class Solution:
    def breadthFirstSearch(self,i,visited,adj,ans):
        q=[i]
        while(q):
            node = q.pop(0)
            ans.append(node)
            for it in adj[node]:
                if visited[it] == 0:
                    visited[it] = 1
                    q.append(it)
    #function to return BFS traversal of given list
    def bfs(self,adj):
        vertex = len(adj)
        ans = []
        visited = [0]*vertex
        for i in range(vertex):
            if visited[i] ==0:
                visited[i] = 1
                self.breadthFirstSearch(i,visited,adj,ans)
        return ans
adj = [
    [1],      # Neighbors of node 0
    [0, 2, 3],# Neighbors of node 1
    [1],      # Neighbors of node 2
    [1]       # Neighbors of node 3
]

# Create object of Solution class and call bfs
sol = Solution()
result = sol.bfs(adj)
print(result)
