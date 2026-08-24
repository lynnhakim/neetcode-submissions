class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        [2, 1, 3] 
        i
        oneup = 2 + 1 = 3 + 3 = 6
                2 + 1 = 3 + 0 = 3
                1
        min = 
        """
        cache = {}

        def dp(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = cost[i] + min(dp(i + 1), dp( i + 2))

            return cache[i]
        return min(dp(0), dp(1))
        
         