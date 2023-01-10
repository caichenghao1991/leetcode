# 98. Validate Binary Search Tree
import sys
from typing import Optional

from tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, sm, lg):
            if not root:
                return True
            if root.val <= sm or root.val >= lg:
                return False
            return helper(root.left, sm, root.val) and helper(root.right, root.val, lg)

        return helper(root, -sys.maxsize, sys.maxsize)
