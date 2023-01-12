# 538. Convert BST to Greater Tree
from typing import Optional
from tree import TreeNode


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0

        def traverse(root):
            if not root:
                return
            traverse(root.right)
            self.s += root.val
            root.val = self.s
            traverse(root.left)

        traverse(root)
        return root
