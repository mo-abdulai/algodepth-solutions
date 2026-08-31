class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {node: [] for node in range(n)}
        
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
        
        component = 0
        for node in range(n):
            if node not in visited:
                component += 1
                dfs(node)
        
        return component

        

                
                

                

