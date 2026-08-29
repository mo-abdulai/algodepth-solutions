class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1 or (row, col) in visited:
                return
            visited.add((row, col))
            queue.append([row, col])

            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visited.add((row,col))
                    queue.append([row, col])
        
        dist = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
            dist += 1


