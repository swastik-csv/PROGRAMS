# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        # Step 1: Get sorted array of node values via in-order traversal
        sorted_values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_values.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        # Step 2: Build a balanced BST from the sorted array recursively
        def build_balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(sorted_values[mid])
            
            node.left = build_balanced_bst(left, mid - 1)
            node.right = build_balanced_bst(mid + 1, right)
            
            return node
            
        return build_balanced_bst(0, len(sorted_values) - 1)