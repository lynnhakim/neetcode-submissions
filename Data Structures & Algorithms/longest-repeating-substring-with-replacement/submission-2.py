class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        BCAABCA k = 2
         l
              r
        1 - 1 = 0< k
        2 - 1 = 1<k
        3 - 1 = 2<=k
        4 - 2 = 2 <=k
        5 - 2 = 3> k
        4 - 2 = 2 <= k
        5 - 3 = 2 <=k


        keep track of freq
        res = 1
        1 - 1 = 0 <= k
        2 - 1 = 1 <= k
        3 - 1 = 2<= k
        update most freq char (A = 2)
        4 - 2 = 2 <=k
        update most freq char (A = 2)
        5 - 3 = 1 <= k 
        6 - 3 = 3 > k
        1. length s 
        2. k = 0, k > s
        """
        freq = {}
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while freq and (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1 )
        return res
            


