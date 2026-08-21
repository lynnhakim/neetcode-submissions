class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        aabc
        xabaabcefgc 
        l  r
        freq = 
        a:2
        b:1
        c:1
           
        """
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) - 1
        freq = {}
        for s in s1:
            freq[s] = 1 + freq.get(s, 0)
        
        while r < len(s2):
            subfreq = {}
            for s in s2[l:r + 1]:
                subfreq[s] = 1 + subfreq.get(s, 0)
            if subfreq == freq: 
                return True
            r += 1
            l += 1
        return False
