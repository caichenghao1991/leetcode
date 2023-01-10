# 104. Maximum Depth of Binary Tree
from collections import deque
from typing import Optional

from tree import TreeNode


class Solution:
    def maxDepth_post(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_pre(self, root: Optional[TreeNode]) -> int:
        depth = 0
        res = 0

        def traverse(root):
            nonlocal depth
            nonlocal res
            if not root: return
            depth += 1
            res = max(depth, res)
            traverse(root.left)
            traverse(root.right)
            depth -= 1

        traverse(root)
        return res

    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root:
            st = deque([(root, 1)])
        else:
            return 0
        while st:
            (n, depth) = st.pop()
            res = max(res, depth)
            if n.left:
                st.append((n.left, depth + 1))
            if n.right:
                st.append((n.right, depth + 1))
        return res
