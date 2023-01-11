# 106. Construct Binary Tree from Inorder and Postorder Traversal
from typing import List, Optional

from tree import TreeNode


class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    #     if not inorder:
    #         return None
    #     v = postorder[-1]
    #     root = TreeNode(v)
    #     x = inorder.index(v)
    #     root.left = self.buildTree(inorder[:x], postorder[:x])
    #
    #     root.right = self.buildTree(inorder[x + 1:], postorder[x:-1])
    #     return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ind = {}
        for i in range(len(inorder)):
            ind[inorder[i]] = i

        def helper(l, r, l2, r2):
            if l > r or l2 > r2: return None
            v = postorder[r2]
            root = TreeNode(v)
            x = ind[v]
            root.left = helper(l, x - 1, l2, l2 + (x - 1 - l))
            root.right = helper(x + 1, r, l2 + (x - l), r2 - 1)
            return root

        return helper(0, len(inorder) - 1, 0, len(inorder) - 1)
