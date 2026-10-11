# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        node_list = []
        def dfs(cur):
            if cur == None: return None
            dfs(cur.left)
            node_list.append(cur.val)
            dfs(cur.right)
        dfs(root)
        return node_list

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        cur = root
        stack = []
        node_list = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                node_list.append(cur.val)
                cur = cur.right
        return node_list

