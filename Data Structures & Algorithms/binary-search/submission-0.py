class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) 
        while l < r: 
            half =( l + r)// 2
            if nums[half] == target:
                return half
            elif nums[half] > target:
                r = half
            else: 
                l = half + 1
        return -1