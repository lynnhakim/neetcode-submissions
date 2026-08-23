class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != "1":
                return 
            if (i, j) in visited:
                return

            visited.add((i, j))

            up = dfs(i + 1, j)
            down = dfs(i - 1, j)
            right = dfs(i, j + 1)
            left = dfs(i, j - 1)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res

