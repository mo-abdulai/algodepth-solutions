class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {node: [] for node in range(n)}
        
        for node1, node2 in  edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for neigbor in adj[node]:
                if neigbor == prev:
                    continue
                
                if not dfs(neigbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n