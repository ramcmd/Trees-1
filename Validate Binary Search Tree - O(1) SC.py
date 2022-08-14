# TC: O(2n) where n is the no of nodes present in the BST
# SC: O(1) (by checking if the previous val is lesser than curr val)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.curr = float("-Inf") 
        self.Flag = True
        self.traversal(root)
        
        return self.Flag
        
        
    def traversal(self, root):
        if root == None:
            return 
        
        # inorder traversal
        
        self.traversal(root.left)
        
        if root.val <= self.curr:
            self.Flag = False
      
        self.curr = root.val
        
        self.traversal(root.right)
        
        
        
        
        
        