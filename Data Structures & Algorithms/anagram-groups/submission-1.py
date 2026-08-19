class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs = [abc, cba, def, bac, efd]
        res = [[abc, cba, bac], [def, efd]]
        ((a 1), (b: 1),(c:1))
        d: 1, e:1, f:1
        {
            ((a 1), (b: 1),(c:1)): [abc]

        }
        if tuple(Counter(abc)) in table: 
            table[tuple(Counter(abc))] 
        """
        anagrams = {}
        for s in strs: 
            freq = tuple(sorted(Counter(s).items()))
            if freq in anagrams: 
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]
        return list(anagrams.values())