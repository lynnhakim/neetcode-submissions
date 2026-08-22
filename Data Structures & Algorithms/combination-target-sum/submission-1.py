class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        [2 5 6 9] target 9
        sub[2 2 2 2]
        """
        res = []
        def backtrack(start, sub):
            if sum(sub) == target :
                res.append(sub[:])
                return
            if sum(sub) > target:
                return
            for i in range(start, len(nums)):
                sub.append(nums[i])
                backtrack(i, sub)
                sub.pop()
        backtrack(0, [])
        return res

            