class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = 0
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))

            time += 1

        return time if fresh == 0 else -1
