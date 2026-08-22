# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root and subroot and root.val == subroot.val:
                right = dfs(root.right, subroot.right) 
                left = dfs(root.left, subroot.left)
                return right and left
            return False

        if not subRoot: return True
        if not root: return False

        if dfs(root, subRoot): return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    