# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
                        3 <-
                1.             2
            4 <-   5 <-     3   
        res = [3, 4]
        3 > 2
        3 > 2 but 3 = root
        1< 3 
        4> 1 and 4 > 3
        5 > 1 and 5> 3
        root
        """
        self.res = 0
        
        def dfs(root, maxVal):

            if not root: 
                return 0
            maxVal = max(maxVal, root.val)
            if root.val >= maxVal:
                self.res += 1
            dfs(root.right, maxVal)
            dfs(root.left, maxVal)
            return self.res
        
        return dfs(root, root.val)
            
                



