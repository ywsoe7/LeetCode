# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        return self.dfs(root, k, visited)
        
        
    def dfs(self, node, k, visited):
        if not node:
            return None
        
        if (k - node.val) in visited:
            return True
        
        visited.add(node.val)
        
        return self.dfs(node.left, k, visited) or self.dfs(node.right, k, visited)