# 617. Merge Two Binary Trees
from typing import Optional

from tree import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        node = TreeNode(v1 + v2)
        l1, r1, l2, r2 = None, None, None, None
        if root1:
            l1, r1 = root1.left, root1.right
        if root2:
            l2, r2 = root2.left, root2.right
        node.left = self.mergeTrees(l1, l2)
        node.right = self.mergeTrees(r1, r2)
        return node
