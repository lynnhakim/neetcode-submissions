class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        res = 0
        max= 0
        for row
            for col
                i, j not in visited and val == 1:
                    r += dfs()
        dfs()
            edge cases: i, j > 0, i, j <len()
                return
            if gird[ij] = 0:
                return
            visited.add((i, j))
            currmax+= 1
            dfs(i + 1, j)
            dfs(i -1 , j)
            dfs(i, j+ 1)
            dfs(i, j - 1)
        visited = (0, 1)(0, 2))
        0, 1
        currmax = 1
        """
        rows = len(grid)
        cols = len(grid[0])
        res, currmax = 0, 0 
        visited = set()
        def dfs(i, j, currmax):

            if i < 0 or j < 0 or i >= rows or  j >= cols:
                return 0
            if grid[i][j] == 0 or (i, j) in visited:
                return 0

            visited.add((i, j))
            up = dfs(i + 1, j, currmax)
            down = dfs(i - 1 , j, currmax)
            right = dfs(i, j+ 1, currmax)
            left = dfs(i, j - 1, currmax)
            
            return 1 + up + down + left + right

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    currmax = dfs(i, j, 0)
                res = max(currmax, res)
        return res


        

