# 404. Sum of Left Leaves
from typing import Optional
from tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l=root.left
        if l and not l.left and not l.right:
            return l.val+self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)