# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        [1]
        [1 3 4]
        2 go right none
        left
        go right none
        left
        1][2 3][4][5]
        [1][2 3][4 5]
        for each sub list, choose [-1]
        """
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[-1])
        
        return res
                