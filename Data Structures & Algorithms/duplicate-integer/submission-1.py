class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        1, 2, 3, 3
        {
        1: 1
        2: 1
        3: 2 > 1 return false
        }
        """
        freq = {}
        for num in nums:
            if num in freq: 
                return True
            freq[num] = 1
        return False