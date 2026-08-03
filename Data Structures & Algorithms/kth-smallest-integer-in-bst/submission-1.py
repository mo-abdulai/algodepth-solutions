# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0
        
        def inOrder(root, k):
            nonlocal count, result

            if not root:
                return
            
            inOrder(root.left, k)
            count += 1
            
            if count == k:
                result = root.val
                return
            
            inOrder(root.right, k)
        
        inOrder(root, k)
        return result
