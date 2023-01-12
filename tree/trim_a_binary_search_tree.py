# 669. Trim a Binary Search Tree
from typing import Optional
from tree import TreeNode


class Solution:
    class Solution:
        def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
            if not root: return None

            if root.val > high:
                return self.trimBST(root.left, low, high)
            elif root.val < low:
                return self.trimBST(root.right, low, high)
            else:
                root.left = self.trimBST(root.left, low, root.val)
                root.right = self.trimBST(root.right, root.val, high)
                return root