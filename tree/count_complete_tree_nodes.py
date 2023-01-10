# Count Complete Tree Nodes             need rework
from typing import Optional

from tree import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        curr = root
        dl, dr = 1, 1
        while curr.left:
            dl += 1
            curr = curr.left
        curr = root
        while curr.right:
            dr += 1
            curr = curr.right
        if dl == dr:
            return 2 ** dl - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
