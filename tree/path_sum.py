# 112. Path Sum
from typing import Optional

from tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False

        def traverse(root, w):
            if not root:
                return
            if not root.left and not root.right:
                if w + root.val == targetSum:
                    self.res = True
                return
            traverse(root.left, w + root.val)
            traverse(root.right, w + root.val)

        traverse(root, 0)
        return self.res
