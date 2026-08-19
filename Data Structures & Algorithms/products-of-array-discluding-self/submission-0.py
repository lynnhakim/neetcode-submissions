class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        pref 1 1 2 8
        post 1 6 24 48
        nums[i - 1] * prefix [i]
        post[i] * nums[-i - 1]
        """
        res = []
        pref, post = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
            post[i] = post[i - 1] * nums[-i]
        for i in range(len(nums)):
            res.append(pref[i] * post[-i-1])
        return res

    
        