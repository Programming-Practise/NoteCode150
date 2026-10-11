# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        node_list = []
        def dfs(cur):
            if cur == None: return None
            dfs(cur.left)
            dfs(cur.right)
            node_list.append(cur.val)
        dfs(root)
        return node_list

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack = [root]
        node_list = []

        while stack:
            node = stack.pop()

            if node:
                node_list.append(node.val)

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

        return node_list[::-1]
