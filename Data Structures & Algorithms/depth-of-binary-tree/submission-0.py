# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root: queue.append(root)
        height = 0
        while len(queue)>0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if(curr.left):queue.append(curr.left)
                if(curr.right):queue.append(curr.right)
            height+=1
        return height