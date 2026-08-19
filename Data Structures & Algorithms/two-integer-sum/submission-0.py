class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums, target
        return i, j 
        nums[i] + nums[j] == target and i != j
        [3, 2, 5, 1] target = 6
        i: target - nums[i]
        3: 0
        4: 1
        1: 2
        5: 3
        
        if nums[table[i]] =  target - nums[i] 
       
        """
        table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in table: 
                return [table[diff], i]
            table[num] = i
