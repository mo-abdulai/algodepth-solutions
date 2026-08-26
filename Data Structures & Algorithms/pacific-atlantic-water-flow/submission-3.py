class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(row, col, visited, prevHeight):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or heights[row][col] < prevHeight:
                return
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])


        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in atl and (row, col) in pac:
                    result.append([row, col])
        
        return result

        