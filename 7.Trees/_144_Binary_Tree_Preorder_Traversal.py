# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []
        def dfs(cur):
            if cur == None: return None
            node_list.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return node_list

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        node_list = []
        while stack:
            node = stack.pop()
            if node:
                node_list.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return node_list 


