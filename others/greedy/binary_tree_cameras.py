# 968. Binary Tree Cameras          need rework
from typing import Optional

from tree import TreeNode


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):  # cover is from parent
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 2 and r == 2:
                return 0
            elif l == 0 or r == 0:
                self.res += 1
                return 1
            elif l == 1 or r == 1:
                return 2

        if dfs(root) == 0:
            self.res += 1
        return self.res
