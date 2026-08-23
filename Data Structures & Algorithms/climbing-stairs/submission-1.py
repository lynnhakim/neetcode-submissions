class Solution:
    def climbStairs(self, n: int) -> int:
        """
                        1 - 2 imp
                3- 2 = 1 - 1 =  0
        4 - 1 = 3 - 1 = 2 - 2 = 0
        4 - 2 = 2 - 2 = 0
                2 - 1 = 1 - 2 imp
                        1 -1  = 0
        

        """
        cache = {}
        res = 0
        def dp(num):
            if num < 0:
                return 0 
            if num in cache: 
                return cache[num]
            if num == 0:
                return 1
            cache[num] =  dp(num - 1) + dp(num - 2)
            return cache[num]
        return dp(n)
            
        
