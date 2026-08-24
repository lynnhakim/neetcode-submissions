class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        """
        
        """
       
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if grid[r][c] == ".":
                    continue
                if grid[r][c] in rows[r] or grid[r][c] in cols[c] or grid[r][c] in squares[(r//3, c//3)]:
                    return False
                

                rows[r].add(grid[r][c])
                cols[c].add(grid[r][c])
                squares[(r//3, c//3)].add(grid[r][c])
        return True
