class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        
        ((())
        """
        res = []
        def backtrack(closed, opened, sub):
            if closed > opened:
                return
            if len(sub) == 2*n:
                res.append(sub)
                return
            
            if opened < n:
                backtrack(closed, opened + 1, sub + "(")
            if closed < opened:
                backtrack(closed + 1, opened, sub+ ")")

            
        backtrack(0,0,"")
        return res
            
