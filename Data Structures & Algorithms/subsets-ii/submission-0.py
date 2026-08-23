class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(sub, i):
            if i == len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            backtrack(sub, i + 1)
            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(sub, i + 1)

            
        backtrack([], 0)
        return res
            
        