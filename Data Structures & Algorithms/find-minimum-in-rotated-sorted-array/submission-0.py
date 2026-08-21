class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2]
        mid
        lo = 0, hi = 5, mid = 0 + 5 // 2 = 2
        nums[2] = 5 > nums[5] = 2 -> lo = 3
        mid = 3 + 5// 2 = 4
        nums[4] = 1 < nums[5] = 2 ->hi = 4
        mid = 3 + 4//2 = 3
        nums[3] =6 > nums[4] = 1 lo = 4
        mid = 4 + 4 //2 = 4
        nums[4] =


        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else: 
                hi = mid
        return nums[lo]
