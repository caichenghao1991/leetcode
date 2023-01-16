# 257. Binary Tree Paths
from typing import Optional, List

from tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res

        def backtrack(root, path):
            if not root: return
            path.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join([str(i) for i in path]))
            backtrack(root.left, path)
            backtrack(root.right, path)
            path.pop()

        backtrack(root, [])
        return res
