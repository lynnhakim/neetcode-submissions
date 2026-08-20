class Solution:
    def trap(self, height: List[int]) -> int:
        """
        0: trap = 0, min(L = 0, R = 3)
        1: min(L = 0, R = 3)  curr = 2 : 0 - 2 < 0 -> trap = 0
        i = 2: min(L = 2, R = 3) curr = 0: 2 - 0 = 2 -> trap += 2
        i = 3: min(L = 2,, R = 3) curr = 3: 3- 3 = 0 -->trap += 0
        i = 4: min(L = 3, R = 3) curr = 1: 3 - 1 = 2--> trap += 2 = 4
        ...
        1. track left max and right max heights
        2. compute min(leftmax , rightmax) - heights[i]
        3. if compute > 0: trap += compute
        
        [0, 0, 2, 3, 3, 3, 3, 3, 3, 3] height[i - 1]
        [0, 1, 2, ]
        """
        leftmax, rightmax = [0],[0]
        trap = 0
        for i in range(1, len(height)):
            leftmax.append(max(height[i - 1], leftmax[i - 1]))
            rightmax.append(max(height[-i], rightmax[i - 1]))

        for i in range(len(height)):
            minimum = min(leftmax[i], rightmax[-i]) - height[i]
            if minimum > 0: 
                trap +=  minimum
        return trap
            