# 530. Minimum Absolute Difference in BST
from typing import Optional

from tree import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return
        less, more = -100000, 100000
        a, b = 100000, 100000
        if root.left:
            curr = root.left
            while curr:
                less = curr.val
                curr = curr.right
            a = self.getMinimumDifference(root.left)
        if root.right:
            curr = root.right
            while curr:
                more = curr.val
                curr = curr.left
            b = self.getMinimumDifference(root.right)
        return min(a, b, root.val - less, more - root.val)
