class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        hash1, hash2 = Counter(s), Counter(t)
        if hash1 == hash2:
            return True
        return False

       