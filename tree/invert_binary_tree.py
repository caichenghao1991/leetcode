# 226. Invert Binary Tree
from tree import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if not root:
        #     return None
        # l = self.invertTree(root.left)
        # r = self.invertTree(root.right)
        # return TreeNode(root.val, left=r, right=l)

        def traverse(root):
            if not root: return
            root.left, root.right = root.right, root.left
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return root
