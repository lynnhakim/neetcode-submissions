class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
      
        
        while r < len(prices): 
            if  prices[l] < prices[r]: 
                curr = prices[r] - prices[l]
                profit = max(curr, profit)
            else: l = r
            r += 1

        return profit
            
            
        