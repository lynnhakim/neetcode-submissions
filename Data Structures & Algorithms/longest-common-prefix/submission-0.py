class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        bat, bag
        i.   i
        if s1[i] == s2[i]:
            append to res
        (bat, bag, bank, band)
        i
        """
        res = ""
        for s in zip(*strs):
            if len(set(s)) == 1:
                res += s[0]
            else: break
        return res
            
                    
            
