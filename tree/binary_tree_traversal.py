# 94. Binary Tree Inorder Traversal
from collections import deque
from typing import List

from tree import TreeNode


class Solution(object):
    def recursive_traversal(self, root: TreeNode) -> List:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res

    @staticmethod
    def inorder_traversal(root):
        res, st = [], []
        curr = root
        while st or curr:  # important not missing curr
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                n = st.pop()
                res.append(n.val)
                curr = n.right
        return res

    @staticmethod
    def preorder_traversal(root):
        res, st = [], deque([root])
        while st:
            n = st.pop()
            if n:
                res.append(n.val)
                st.append(n.right)
                st.append(n.left)
        return res

    @staticmethod
    def postorder_traversal(root):
        res, st = [], deque([root])
        while st:
            n = st.pop()
            if n:
                res.append(n.val)
                st.append(n.left)
                st.append(n.right)
        return res[::-1]