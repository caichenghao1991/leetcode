# 450. Delete Node in a BST              need rework
from typing import Optional

from tree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root