class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return

            grid[x][y] = '0'
            dfs(x - 1, y), dfs(x + 1, y)
            dfs(x, y - 1), dfs(x, y + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    lands += 1
                    dfs(i, j)

        return lands