# TC: O(2n) where n is the no of nodes present in the BST
# SC: O(n) (we are storing the val in arr and checking whether it is in sorted order) in this case, but can be reduced to O(1) (by checking if the previous val is lesser than curr val)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.arr = []
        self.traversal(root)
        
        for i in range(1, len(self.arr)):
            if not self.arr[i] > self.arr[i-1]:
                return False
        
        return True
                
        
        
    def traversal(self, root):
        if root == None:
            return 
        
        # inorder traversal
        
        self.traversal(root.left)
        
        self.arr.append(root.val)
        
        self.traversal(root.right)
        
        
        
        
        
        