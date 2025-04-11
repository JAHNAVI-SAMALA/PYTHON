class Solution:
    def depthFirstSearch(self,node,adj,vis,ans):
        vis[node] = 1
        ans.append(node)
        for it in adj[node]:
            if vis[it] == 0:
                self.depthFirstSearch(it,adj,vis,ans)
    def dfs(self,adj):
        nodes = len(adj)
        vis = [0]*nodes
        ans = []
        for i in range(nodes):
            if vis[i] == 0:
                self.depthFirstSearch(i,adj,vis,ans)
        return ans
adj = [[1,4],[0,2,3],[1],[1],[0,5,7],[4,6],[5,7],[4,6]]
sol = Solution()
print(sol.dfs(adj))
