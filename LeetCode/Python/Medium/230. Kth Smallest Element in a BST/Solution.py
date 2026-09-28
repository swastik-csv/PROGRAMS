# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the current node from the stack
            curr = stack.pop()
            
            # Decrement k as we visit each node in ascending order
            k -= 1
            if k == 0:
                return curr.val
            
            # Visit the right subtree
            curr = curr.right