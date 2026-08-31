class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {n: [] for n in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
        

        component = 0
        for node in range(n):
            if not node in visited:
                component += 1
                dfs(node)
        
        return component

        

        

                
                

                

