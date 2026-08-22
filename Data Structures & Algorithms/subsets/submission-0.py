class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
        res[[],[1], 
        path [1]

        """
        res = []
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i + 1, path)
                
                path.pop()

        backtrack(0, [])
        return res

                
            

