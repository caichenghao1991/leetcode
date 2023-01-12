# 701. Insert into a Binary Search Tree
from typing import Optional

from tree import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # n = TreeNode(val)
        # if not root: return n
        # curr = root
        # while curr:
        #     if val > curr.val:
        #         if not curr.right:
        #             curr.right = n
        #             break
        #         curr = curr.right
        #         continue
        #     if val < curr.val:
        #         if not curr.left:
        #             curr.left = n
        #             break
        #         curr = curr.left
        #         continue
        # return root

        if not root: 
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
