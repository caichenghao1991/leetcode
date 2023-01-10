# 101. Symmetric Tree
from typing import Optional

from tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.f = True

        def traverse(l, r):
            if (not l and r) or (not r and l):
                self.f = False
                return
            elif not l and not r:
                return
            if l.val != r.val:
                self.f = False
                return
            traverse(l.right, r.left)
            traverse(l.left, r.right)

        traverse(root, root)
        return self.f

        # def postorder(l, r):
        #     if (not l and r) or (not r and l):
        #         return False
        #     elif not l and not r:
        #         return True
        #     return postorder(l.right, r.left) and postorder(l.left, r.right) and l.val == r.val
        # return postorder(root, root)
