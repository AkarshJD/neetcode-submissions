# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        #order of the operations/conditions is very important
        if not t: return True
        if not s: return False   
        if self.isSameTree(s,t):
            return True
        #tricky
        #compare t to the left subtree of s or t to the right subtree of s
        return (self.isSubtree(s.left,t) or 
                self.isSubtree(s.right,t))


    

